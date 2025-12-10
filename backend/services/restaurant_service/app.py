from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# MySQL Configuration - Restaurant Service Database
db_config = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'database': os.getenv('RESTAURANT_DB_NAME', 'restaurant_db'),
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

# ==================== RESTAURANT CRUD ====================

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    """Get all restaurants"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM restaurants')
        restaurants = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(restaurants), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    """Get specific restaurant"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM restaurants WHERE id = %s', (restaurant_id,))
        restaurant = cursor.fetchone()
        cursor.close()
        conn.close()

        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404
        return jsonify(restaurant), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/restaurants', methods=['POST'])
def create_restaurant():
    """Create new restaurant"""
    data = request.get_json()
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        query = 'INSERT INTO restaurants (name, location) VALUES (%s, %s)'
        cursor.execute(query, (data.get('name'), data.get('location')))
        conn.commit()
        restaurant_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return jsonify({'id': restaurant_id, 'message': 'Restaurant created successfully'}), 201
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/restaurants/<int:restaurant_id>', methods=['PUT'])
def update_restaurant(restaurant_id):
    """Update restaurant"""
    data = request.get_json()
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        query = 'UPDATE restaurants SET name = %s, location = %s WHERE id = %s'
        cursor.execute(query, (data.get('name'), data.get('location'), restaurant_id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Restaurant updated successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    """Delete restaurant"""
    conn = get_db_connection()
    if not conn:
        return jsonify({'error': 'Database connection failed'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM restaurants WHERE id = %s', (restaurant_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Restaurant deleted successfully'}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check"""
    return jsonify({'status': 'Restaurant Service is running'}), 200

if __name__ == '__main__':
    port = int(os.getenv('RESTAURANT_SERVICE_PORT', 5002))
    app.run(debug=True, host='0.0.0.0', port=port)
