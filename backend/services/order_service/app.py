from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# MySQL Configuration
db_config = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'database': os.getenv('MYSQL_DATABASE', 'pastry_db'),
    'port': int(os.getenv('MYSQL_PORT', 3306))
}

# Service URLs
CUSTOMER_SERVICE_URL = os.getenv('CUSTOMER_SERVICE_URL', 'http://localhost:5001')
RESTAURANT_SERVICE_URL = os.getenv('RESTAURANT_SERVICE_URL', 'http://localhost:5002')
MENU_SERVICE_URL = os.getenv('MENU_SERVICE_URL', 'http://localhost:5003')

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def validate_customer(customer_id):
    """Validate customer exists in Customer Service"""
    try:
        response = requests.get(f'{CUSTOMER_SERVICE_URL}/customers/{customer_id}', timeout=5)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print(f"ERROR: Cannot connect to Customer Service at {CUSTOMER_SERVICE_URL}")
        return False
    except requests.exceptions.Timeout:
        print(f"ERROR: Customer Service request timeout")
        return False
    except Exception as e:
        print(f"ERROR: Customer validation failed: {str(e)}")
        return False

def validate_menu_item(menu_id):
    """Validate menu item exists in Menu Service"""
    try:
        response = requests.get(f'{MENU_SERVICE_URL}/menus/{menu_id}', timeout=5)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        print(f"ERROR: Cannot connect to Menu Service at {MENU_SERVICE_URL}")
        return False
    except requests.exceptions.Timeout:
        print(f"ERROR: Menu Service request timeout")
        return False
    except Exception as e:
        print(f"ERROR: Menu validation failed: {str(e)}")
        return False

def create_customer(name, email, phone):
    """Create customer in Customer Service and return customer_id"""
    try:
        response = requests.post(
            f'{CUSTOMER_SERVICE_URL}/customers',
            json={'name': name, 'email': email, 'phone': phone},
            timeout=5
        )
        if response.status_code == 201:
            customer_data = response.json()
            return customer_data.get('id')
        return None
    except requests.exceptions.ConnectionError:
        print(f"ERROR: Cannot connect to Customer Service at {CUSTOMER_SERVICE_URL}")
        return None
    except requests.exceptions.Timeout:
        print(f"ERROR: Customer Service request timeout")
        return None
    except Exception as e:
        print(f"ERROR: Customer creation failed: {str(e)}")
        return None

# ==================== ORDER CRUD ====================

@app.route('/orders', methods=['GET'])
def get_orders():
    """Get orders based on role"""
    role = request.args.get('role', 'customer')
    username = request.args.get('username', '')
    
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        if role == 'admin':
            cursor.execute('SELECT * FROM orders ORDER BY id DESC')
        else:
            # For customer, get their orders
            cursor.execute('SELECT * FROM orders WHERE customer_username = %s ORDER BY id DESC', (username,))
        
        orders = cursor.fetchall()
        
        # Enrich orders with items and menu names
        for order in orders:
            cursor.execute('''
                SELECT oi.menu_id, oi.quantity, oi.price, mi.name as menu_name
                FROM order_items oi
                LEFT JOIN menu_items mi ON oi.menu_id = mi.id
                WHERE oi.order_id = %s
            ''', (order['id'],))
            order['items'] = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return jsonify(orders), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Get specific order with items"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM orders WHERE id = %s', (order_id,))
        order = cursor.fetchone()

        if not order:
            cursor.close()
            conn.close()
            return jsonify({'error': 'Order not found'}), 404

        # Get order items with menu names
        cursor.execute('''
            SELECT oi.menu_id, oi.quantity, oi.price, mi.name as menu_name
            FROM order_items oi
            LEFT JOIN menu_items mi ON oi.menu_id = mi.id
            WHERE oi.order_id = %s
        ''', (order_id,))
        order['items'] = cursor.fetchall()
        
        cursor.close()
        conn.close()
        return jsonify(order), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders', methods=['POST'])
def create_order():
    """Create new order (Consumer calls other services for validation)"""
    data = request.get_json()
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        # Get or create customer
        customer_id = data.get('customer_id')
        
        # If customer_id not provided, try to create customer from customer info
        if not customer_id:
            customer_name = data.get('customer_name')
            customer_email = data.get('customer_email')
            customer_phone = data.get('customer_phone')
            
            if customer_name and customer_email and customer_phone:
                # Auto-create customer
                customer_id = create_customer(customer_name, customer_email, customer_phone)
                if not customer_id:
                    return jsonify({
                        'error': 'Failed to create customer record',
                        'details': 'Please check if Customer Service is running on port 5001'
                    }), 503
            else:
                return jsonify({
                    'error': 'customer_id is required, or provide customer_name, customer_email, and customer_phone to auto-create customer'
                }), 400
        
        # Validate customer exists
        if not validate_customer(customer_id):
            return jsonify({
                'error': f'Customer {customer_id} not found or Customer Service is not available',
                'details': 'Please check if Customer Service is running on port 5001'
            }), 404

        # Validate all menu items
        items = data.get('items', [])
        if not items:
            return jsonify({'error': 'Order must contain at least one item'}), 400
        
        for item in items:
            menu_id = item.get('menu_id')
            if not menu_id:
                return jsonify({'error': 'Each item must have a menu_id'}), 400
            if not validate_menu_item(menu_id):
                return jsonify({
                    'error': f'Menu item {menu_id} not found or Menu Service is not available',
                    'details': 'Please check if Menu Service is running on port 5003'
                }), 404

        cursor = conn.cursor()
        
        # Create order
        query = '''INSERT INTO orders 
                   (customer_id, customer_username, customer_name, customer_email, 
                    customer_phone, delivery_address, payment_method, total_price, tax, status) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        
        cursor.execute(query, (
            customer_id,
            data.get('username'),
            data.get('customer_name'),
            data.get('customer_email'),
            data.get('customer_phone'),
            data.get('delivery_address'),
            data.get('payment_method'),
            data.get('total_price'),
            data.get('tax'),
            'on_process'
        ))
        
        order_id = cursor.lastrowid
        
        # Create order items
        for item in items:
            item_query = 'INSERT INTO order_items (order_id, menu_id, quantity, price) VALUES (%s, %s, %s, %s)'
            cursor.execute(item_query, (
                order_id,
                item.get('menu_id'),
                item.get('quantity'),
                item.get('price')
            ))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({
            'id': order_id,
            'message': 'Order created successfully',
            'status': 'on_process'
        }), 201
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    """Update order"""
    data = request.get_json()
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        query = '''UPDATE orders SET customer_name = %s, customer_email = %s, 
                   customer_phone = %s, delivery_address = %s, payment_method = %s, 
                   total_price = %s, tax = %s WHERE id = %s'''
        
        cursor.execute(query, (
            data.get('customer_name'),
            data.get('customer_email'),
            data.get('customer_phone'),
            data.get('delivery_address'),
            data.get('payment_method'),
            data.get('total_price'),
            data.get('tax'),
            order_id
        ))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Order updated successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>/status', methods=['PATCH'])
def update_order_status(order_id):
    """Update order status"""
    data = request.get_json()
    new_status = data.get('status')
    
    valid_statuses = ['on_process', 'on_delivery', 'delivered']
    if new_status not in valid_statuses:
        return jsonify({'error': f'Invalid status. Must be one of: {valid_statuses}'}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE orders SET status = %s WHERE id = %s', (new_status, order_id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Order status updated successfully', 'status': new_status}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Delete order"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        # Delete order items first
        cursor.execute('DELETE FROM order_items WHERE order_id = %s', (order_id,))
        # Delete order
        cursor.execute('DELETE FROM orders WHERE id = %s', (order_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Order deleted successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check"""
    return jsonify({'status': 'Order Service is running'}), 200

if __name__ == '__main__':
    port = int(os.getenv('ORDER_SERVICE_PORT', 5004))
    app.run(debug=True, host='0.0.0.0', port=port)
