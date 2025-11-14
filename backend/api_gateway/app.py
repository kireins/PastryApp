from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

app = Flask(__name__)

# JWT Configuration
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_super_secret_jwt_key_change_this_in_production')
app.config['JWT_ALGORITHM'] = os.getenv('JWT_ALGORITHM', 'HS256')

jwt = JWTManager(app)
CORS(app)

# Configure JWT token expiration (24 hours)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)

# JWT Error Handlers
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({'error': 'Token has expired. Please login again.'}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({'error': f'Invalid token: {str(error)}'}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({'error': 'Authorization token is missing. Please login first.'}), 401

# Service URLs
CUSTOMER_SERVICE_URL = os.getenv('CUSTOMER_SERVICE_URL', 'http://localhost:5001')
RESTAURANT_SERVICE_URL = os.getenv('RESTAURANT_SERVICE_URL', 'http://localhost:5002')
MENU_SERVICE_URL = os.getenv('MENU_SERVICE_URL', 'http://localhost:5003')
ORDER_SERVICE_URL = os.getenv('ORDER_SERVICE_URL', 'http://localhost:5004')

# Hardcoded credentials for demo (in production, validate against database)
USERS = {
    'customer': {'password': 'iamcustomer', 'role': 'customer'},
    'admin': {'password': 'iamadmin', 'role': 'admin'}
}

# Login endpoint
@app.route('/api/login', methods=['POST'])
def login():
    """
    Login endpoint that generates JWT token
    Server determines user role from database, not from request
    Expected JSON: { "username": "customer", "password": "iamcustomer" }
    """
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate credentials
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if username not in USERS or USERS[username]['password'] != password:
        return jsonify({'error': 'Invalid credentials'}), 401

    # Server determines role from database, not from user input
    role = USERS[username]['role']

    # Create JWT token with role claim
    access_token = create_access_token(
        identity=username,
        additional_claims={'role': role}
    )

    # Calculate expiration time
    expires_at = datetime.utcnow() + timedelta(hours=24)

    return jsonify({
        'access_token': access_token,
        'token_type': 'Bearer',
        'expires_in': 86400,  # 24 hours in seconds
        'expires_at': expires_at.isoformat(),
        'username': username,
        'role': role,
        'message': f'Successfully logged in as {role}'
    }), 200

# ==================== CUSTOMER SERVICE ROUTES ====================

@app.route('/api/customers', methods=['GET'])
@jwt_required()
def get_customers():
    """Get all customers (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    response = requests.get(f'{CUSTOMER_SERVICE_URL}/customers')
    return response.json(), response.status_code

@app.route('/api/customers/<int:customer_id>', methods=['GET'])
@jwt_required()
def get_customer(customer_id):
    """Get specific customer"""
    response = requests.get(f'{CUSTOMER_SERVICE_URL}/customers/{customer_id}')
    return response.json(), response.status_code

@app.route('/api/customers', methods=['POST'])
def create_customer():
    """Create new customer"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        response = requests.post(f'{CUSTOMER_SERVICE_URL}/customers', json=data, timeout=10)
        
        try:
            return response.json(), response.status_code
        except ValueError:
            return jsonify({
                'error': f'Customer service returned invalid response: {response.status_code}',
                'details': response.text[:200]
            }), response.status_code
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to Customer Service. Please check if it is running on port 5001'}), 503
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Customer Service request timeout'}), 504
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/customers/<int:customer_id>', methods=['PUT'])
@jwt_required()
def update_customer(customer_id):
    """Update customer"""
    data = request.get_json()
    response = requests.put(f'{CUSTOMER_SERVICE_URL}/customers/{customer_id}', json=data)
    return response.json(), response.status_code

@app.route('/api/customers/<int:customer_id>', methods=['DELETE'])
@jwt_required()
def delete_customer(customer_id):
    """Delete customer (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    response = requests.delete(f'{CUSTOMER_SERVICE_URL}/customers/{customer_id}')
    return response.json(), response.status_code

# ==================== RESTAURANT SERVICE ROUTES ====================

@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
    """Get all restaurants"""
    response = requests.get(f'{RESTAURANT_SERVICE_URL}/restaurants')
    return response.json(), response.status_code

@app.route('/api/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    """Get specific restaurant"""
    response = requests.get(f'{RESTAURANT_SERVICE_URL}/restaurants/{restaurant_id}')
    return response.json(), response.status_code

@app.route('/api/restaurants', methods=['POST'])
@jwt_required()
def create_restaurant():
    """Create new restaurant (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    response = requests.post(f'{RESTAURANT_SERVICE_URL}/restaurants', json=data)
    return response.json(), response.status_code

@app.route('/api/restaurants/<int:restaurant_id>', methods=['PUT'])
@jwt_required()
def update_restaurant(restaurant_id):
    """Update restaurant (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    response = requests.put(f'{RESTAURANT_SERVICE_URL}/restaurants/{restaurant_id}', json=data)
    return response.json(), response.status_code

@app.route('/api/restaurants/<int:restaurant_id>', methods=['DELETE'])
@jwt_required()
def delete_restaurant(restaurant_id):
    """Delete restaurant (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    response = requests.delete(f'{RESTAURANT_SERVICE_URL}/restaurants/{restaurant_id}')
    return response.json(), response.status_code

# ==================== MENU SERVICE ROUTES ====================

@app.route('/api/menus', methods=['GET'])
def get_menus():
    """Get all menu items"""
    response = requests.get(f'{MENU_SERVICE_URL}/menus')
    return response.json(), response.status_code

@app.route('/api/menus/<int:menu_id>', methods=['GET'])
def get_menu(menu_id):
    """Get specific menu item"""
    response = requests.get(f'{MENU_SERVICE_URL}/menus/{menu_id}')
    return response.json(), response.status_code

@app.route('/api/restaurants/<int:restaurant_id>/menus', methods=['GET'])
def get_restaurant_menus(restaurant_id):
    """Get menu items for specific restaurant"""
    response = requests.get(f'{MENU_SERVICE_URL}/restaurants/{restaurant_id}/menus')
    return response.json(), response.status_code

@app.route('/api/menus', methods=['POST'])
@jwt_required()
def create_menu():
    """Create new menu item (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    response = requests.post(f'{MENU_SERVICE_URL}/menus', json=data)
    return response.json(), response.status_code

@app.route('/api/menus/<int:menu_id>', methods=['PUT'])
@jwt_required()
def update_menu(menu_id):
    """Update menu item (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    response = requests.put(f'{MENU_SERVICE_URL}/menus/{menu_id}', json=data)
    return response.json(), response.status_code

@app.route('/api/menus/<int:menu_id>', methods=['DELETE'])
@jwt_required()
def delete_menu(menu_id):
    """Delete menu item (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    response = requests.delete(f'{MENU_SERVICE_URL}/menus/{menu_id}')
    return response.json(), response.status_code

# ==================== ORDER SERVICE ROUTES ====================

@app.route('/api/orders', methods=['GET'])
@jwt_required()
def get_orders():
    """Get all orders (Admin) or user's orders (Customer)"""
    claims = get_jwt()
    response = requests.get(f'{ORDER_SERVICE_URL}/orders', params={'role': claims['role'], 'username': claims['sub']})
    return response.json(), response.status_code

@app.route('/api/orders/<int:order_id>', methods=['GET'])
@jwt_required()
def get_order(order_id):
    """Get specific order"""
    response = requests.get(f'{ORDER_SERVICE_URL}/orders/{order_id}')
    return response.json(), response.status_code

@app.route('/api/orders', methods=['POST'])
@jwt_required()
def create_order():
    """Create new order"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        data['username'] = get_jwt_identity()
        response = requests.post(f'{ORDER_SERVICE_URL}/orders', json=data, timeout=10)
        
        try:
            return response.json(), response.status_code
        except ValueError:
            # If response is not JSON
            return jsonify({
                'error': f'Order service returned invalid response: {response.status_code}',
                'details': response.text[:200]
            }), response.status_code
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Cannot connect to Order Service. Please check if it is running on port 5004'}), 503
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Order Service request timeout'}), 504
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/orders/<int:order_id>', methods=['PUT'])
@jwt_required()
def update_order(order_id):
    """Update order (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    response = requests.put(f'{ORDER_SERVICE_URL}/orders/{order_id}', json=data)
    return response.json(), response.status_code

@app.route('/api/orders/<int:order_id>', methods=['DELETE'])
@jwt_required()
def delete_order(order_id):
    """Delete order (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    response = requests.delete(f'{ORDER_SERVICE_URL}/orders/{order_id}')
    return response.json(), response.status_code

@app.route('/api/orders/<int:order_id>/status', methods=['PATCH'])
@jwt_required()
def update_order_status(order_id):
    """Update order status (Admin only)"""
    claims = get_jwt()
    if claims['role'] != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    response = requests.patch(f'{ORDER_SERVICE_URL}/orders/{order_id}/status', json=data)
    return response.json(), response.status_code

# Health check
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'API Gateway is running'}), 200

if __name__ == '__main__':
    port = int(os.getenv('API_GATEWAY_PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
