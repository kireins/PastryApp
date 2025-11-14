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

# ==================== MENU CRUD ====================

@app.route('/menus', methods=['GET'])
def get_menus():
    """Get all menu items"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM menu_items')
        menus = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(menus), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/menus/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    """Get specific menu item"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM menu_items WHERE id = %s', (menu_id,))
        menu = cursor.fetchone()
        cursor.close()
        conn.close()

        if not menu:
            return jsonify({'error': 'Menu item not found'}), 404
        return jsonify(menu), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/restaurants/<int:restaurant_id>/menus', methods=['GET'])
def get_restaurant_menus(restaurant_id):
    """Get menu items for specific restaurant"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM menu_items WHERE restaurant_id = %s', (restaurant_id,))
        menus = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(menus), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/menus', methods=['POST'])
def create_menu():
    """Create new menu item"""
    data = request.get_json()
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        query = 'INSERT INTO menu_items (restaurant_id, name, price, description) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (
            data.get('restaurant_id'),
            data.get('name'),
            data.get('price'),
            data.get('description', '')
        ))
        conn.commit()
        menu_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return jsonify({'id': menu_id, 'message': 'Menu item created successfully'}), 201
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/menus/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    """Update menu item"""
    data = request.get_json()
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        query = 'UPDATE menu_items SET name = %s, price = %s, description = %s WHERE id = %s'
        cursor.execute(query, (
            data.get('name'),
            data.get('price'),
            data.get('description', ''),
            menu_id
        ))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Menu item updated successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/menus/<int:menu_id>', methods=['DELETE'])
def delete_menu(menu_id):
    """Delete menu item"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM menu_items WHERE id = %s', (menu_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Menu item deleted successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check"""
    return jsonify({'status': 'Menu Service is running'}), 200

if __name__ == '__main__':
    port = int(os.getenv('MENU_SERVICE_PORT', 5003))
    app.run(debug=True, host='0.0.0.0', port=port)
