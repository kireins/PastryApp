from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
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

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# ==================== CUSTOMER CRUD ====================

@app.route('/customers', methods=['GET'])
def get_customers():
    """Get all customers"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM customers')
        customers = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(customers), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get specific customer"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM customers WHERE id = %s', (customer_id,))
        customer = cursor.fetchone()
        cursor.close()
        conn.close()

        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
        return jsonify(customer), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/customers', methods=['POST'])
def create_customer():
    """Create new customer"""
    data = request.get_json()
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        query = 'INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)'
        cursor.execute(query, (data.get('name'), data.get('email'), data.get('phone')))
        conn.commit()
        customer_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return jsonify({'id': customer_id, 'message': 'Customer created successfully'}), 201
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    """Update customer"""
    data = request.get_json()
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        query = 'UPDATE customers SET name = %s, email = %s, phone = %s WHERE id = %s'
        cursor.execute(query, (data.get('name'), data.get('email'), data.get('phone'), customer_id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Customer updated successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """Delete customer"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM customers WHERE id = %s', (customer_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Customer deleted successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check"""
    return jsonify({'status': 'Customer Service is running'}), 200

if __name__ == '__main__':
    port = int(os.getenv('CUSTOMER_SERVICE_PORT', 5001))
    app.run(debug=True, host='0.0.0.0', port=port)
