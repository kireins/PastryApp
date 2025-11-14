# 🥐 Pastry Delivery - Food Delivery System

A complete microservices-based food delivery application for the Pastry restaurant built with Flask, featuring JWT authentication with role-based access control, API Gateway, dual-role frontend (Customer & Admin), and real-time order management.

## ✨ Key Features

### 🎯 Dual-Role System
- **Customer Role**: Browse menu, place orders, track order status with receipt-style details
- **Admin Role**: Full dashboard with all orders, status management, CRUD operations

### 🏗️ 4 Independent Microservices
- **Customer Service** (Provider) - Manages customer data
- **Restaurant Service** (Provider) - Manages restaurant information
- **Menu Service** (Provider) - Manages menu items
- **Order Service** (Consumer) - Manages orders with service validation

### 🔐 API Gateway with JWT Authentication
- Role-based JWT tokens for Customer & Admin access
- Service-to-service communication
- Centralized routing and authorization

### 📊 Advanced Order Status Tracking
- on_process: Order being prepared
- on_delivery: Order on the way
- delivered: Order completed

### 🎨 Animated Frontend
- **Customer Interface** (`index.html`) - Menu browsing with smooth animations
- **Admin Dashboard** (`admin.html`) - Real-time order management
- Color palette: Brown (#6c3f2b), Pink (#e15f8c), Green (#b4d96f), Cream (#fef8f1)
- Responsive design with micro-animations

### 📱 Real-Time Features
- Auto-refresh dashboard every 10 seconds
- Live order status updates
- Receipt-style order confirmation
- Order history tracking

## 🛠️ Technologies

| Component | Technology | Version |
|-----------|-----------|---------|
| Backend Framework | Flask | 3.0.0 |
| Authentication | Flask-JWT-Extended | 4.5.3 |
| CORS Support | Flask-CORS | 4.0.0 |
| HTTP Requests | requests | 2.31.0 |
| Environment | python-dotenv | 1.0.0 |
| Database | MySQL | 5.7+ |
| Python | Python | 3.8+ |

## 📦 Project Structure

```
PastryApp/
├── backend/
│   ├── api_gateway/
│   │   └── app.py                  # Main API Gateway with JWT auth
│   ├── services/
│   │   ├── customer_service/
│   │   │   └── app.py              # Customer CRUD operations
│   │   ├── restaurant_service/
│   │   │   └── app.py              # Restaurant management
│   │   ├── menu_service/
│   │   │   └── app.py              # Menu items management
│   │   └── order_service/
│   │       └── app.py              # Order management (Consumer)
│   ├── requirements.txt            # Python dependencies
│   ├── init_db.py                  # Database initialization
│   └── .env                        # Environment configuration
├── frontend/
│   ├── index.html                  # Customer interface with animations
│   ├── admin.html                  # Admin dashboard with animations
│   └── README.md                   # This file
└── documentation/
    └── Pastry_API.postman_collection.json
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- MySQL Server 5.7 or higher
- Node.js (optional, for frontend development)
- Postman (for API testing)

### Installation Steps

#### 1. Clone or Setup Project

```bash
cd /path/to/PastryApp
```

#### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

#### 4. Configure Environment Variables

Edit `backend/.env`:

```env
# Flask Environment
FLASK_ENV=development
FLASK_DEBUG=True

# JWT Configuration
JWT_SECRET_KEY=your_super_secret_jwt_key_change_this_in_production
JWT_ALGORITHM=HS256

# Microservices Ports
API_GATEWAY_PORT=5000
CUSTOMER_SERVICE_PORT=5001
RESTAURANT_SERVICE_PORT=5002
MENU_SERVICE_PORT=5003
ORDER_SERVICE_PORT=5004

# Microservices Base URLs
CUSTOMER_SERVICE_URL=http://localhost:5001
RESTAURANT_SERVICE_URL=http://localhost:5002
MENU_SERVICE_URL=http://localhost:5003
ORDER_SERVICE_URL=http://localhost:5004

# MySQL Configuration
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=pastry_db
MYSQL_PORT=3306
```

#### 5. Initialize Database

```bash
python backend/init_db.py
```

This will create:
- Database: `pastry_db`
- Tables: customers, restaurants, menu_items, orders, order_items
- Sample data: 2 customers, 1 restaurant, 4 menu items

#### 6. Start Microservices

Open 5 terminal windows and run each service:

**Terminal 1 - API Gateway:**
```bash
cd backend/api_gateway
python app.py
```

**Terminal 2 - Customer Service:**
```bash
cd backend/services/customer_service
python app.py
```

**Terminal 3 - Restaurant Service:**
```bash
cd backend/services/restaurant_service
python app.py
```

**Terminal 4 - Menu Service:**
```bash
cd backend/services/menu_service
python app.py
```

**Terminal 5 - Order Service:**
```bash
cd backend/services/order_service
python app.py
```

#### 7. Access Frontend

Open a web server for the frontend. You can use Python's built-in server:

```bash
cd frontend
python3 -m http.server 8000
```

Then visit:
- **Customer**: http://localhost:8000/index.html
- **Admin**: http://localhost:8000/admin.html

## 🔑 Default Credentials

### Customer Login
- **Username**: `customer`
- **Password**: `iamcustomer`
- **Role**: Customer

### Admin Login
- **Username**: `admin`
- **Password**: `iamadmin`
- **Role**: Admin

## 📖 Usage Guide

### Customer Interface (`index.html`)

#### 1. Login
1. Click **"Login"** button in navigation
2. Enter credentials:
   - Username: `customer`
   - Password: `iamcustomer`
   - Role: Customer
3. Receive JWT customer token (stored in localStorage)

#### 2. Browse Menu
- View pastry collection in responsive grid
- Each card displays:
  - Item name and description
  - Price in Rupiah
  - "Add to Cart" button with hover animations

#### 3. Manage Cart (Sidebar)
- View all items in cart
- See quantity and subtotal per item
- Remove items with animated delete button
- Real-time calculation of:
  - Subtotal
  - Tax (5%)
  - Total price

#### 4. Place Order
1. Add items to cart
2. Scroll to "Delivery Details" form
3. Fill in:
   - Customer Name
   - Email Address
   - Phone Number
   - Delivery Address
   - Payment Method (Cash on Delivery or QR Payment)
4. Click **"Place Order"**
5. Receipt modal appears with order confirmation

#### 5. Track Orders
- "Your Orders" section shows all your orders
- Each order displays:
  - Order ID and status
  - Itemized breakdown
  - Customer & delivery info
  - Status badges (on_process, on_delivery, delivered)
- Auto-refreshes every 10 seconds

### Admin Dashboard (`admin.html`)

#### 1. Admin Login
1. On customer page, click **"Login"**
2. Enter:
   - Username: `admin`
   - Password: `iamadmin`
   - Role: Admin (select from dropdown)
3. Automatically redirects to `admin.html`

#### 2. Dashboard Overview
View statistics:
- Total Orders count
- On Process count
- On Delivery count
- Delivered count
- Average orders and pending deliveries

#### 3. Orders Management Table
Features:
- **Columns**: Order ID, Customer, Items, Total, Status, Address, Actions
- **Sorting**: Click status to change
- **Search**: Find orders by ID
- **Filter**: Filter by status (on_process, on_delivery, delivered)
- **Refresh**: Manual refresh or auto-refreshes every 10 seconds

#### 4. Update Order Status
1. Click on status badge (animated chip)
2. Dropdown menu appears with options:
   - On Process
   - On Delivery
   - Delivered
3. Click desired status
4. Status updates immediately with smooth animation
5. Table refreshes

#### 5. View Order Details
1. Click **"View"** button on any order
2. Modal popup displays:
   - Order information with status
   - Customer details
   - Delivery address
   - All ordered items with quantities and prices
   - Payment method
   - Subtotal, tax, and total

#### 6. Delete Orders
1. Click **"Delete"** button on any order
2. Confirm deletion
3. Order removed from system

#### 7. Real-Time Updates
- Dashboard auto-refreshes every 10 seconds
- Live status tracking across all orders
- Responsive design for mobile viewing

## 🎨 Design & Animations

### Color Palette
- **Brown Dark**: #6c3f2b (Primary accent)
- **Pink Vibrant**: #e15f8c (Call-to-action)
- **Green Base**: #b4d96f (Success/buttons)
- **Pink Light**: #f1d2de (Backgrounds)
- **Cream**: #fef8f1 (Main background)
- **Black**: #1a1a1a (Text)

### Animation Types
1. **Fade In/Out**: Modal and element appearances
2. **Slide In/Out**: Navigation and sidebar animations
3. **Scale Up**: Card hovering effects
4. **Pulse**: Order status indicators
5. **Rotate**: Refresh button hover
6. **Smooth Transitions**: All interactive elements

## 🔌 API Endpoints

### Authentication
```
POST /api/login
  Body: { username, password, role }
  Returns: { access_token, username, role }
```

### Customers
```
GET /api/customers                    # Get all (Admin only)
GET /api/customers/<id>               # Get specific customer
POST /api/customers                   # Create customer
PUT /api/customers/<id>               # Update customer
DELETE /api/customers/<id>            # Delete customer (Admin only)
```

### Restaurants
```
GET /api/restaurants                  # Get all restaurants
GET /api/restaurants/<id>             # Get specific restaurant
POST /api/restaurants                 # Create (Admin only)
PUT /api/restaurants/<id>             # Update (Admin only)
DELETE /api/restaurants/<id>          # Delete (Admin only)
```

### Menu Items
```
GET /api/menus                        # Get all menu items
GET /api/menus/<id>                   # Get specific item
GET /api/restaurants/<id>/menus       # Get restaurant menus
POST /api/menus                       # Create menu item (Admin only)
PUT /api/menus/<id>                   # Update menu item (Admin only)
DELETE /api/menus/<id>                # Delete menu item (Admin only)
```

### Orders
```
GET /api/orders                       # Get orders (filtered by role)
GET /api/orders/<id>                  # Get specific order with items
POST /api/orders                      # Create new order
PUT /api/orders/<id>                  # Update order
PATCH /api/orders/<id>/status         # Update order status (Admin only)
DELETE /api/orders/<id>               # Delete order (Admin only)
```

## 📊 Default Data

### Customers
| ID | Name | Email | Phone |
|---|---|---|---|
| 1 | John Doe | john@example.com | 081234567890 |
| 2 | Jane Smith | jane@example.com | 082345678901 |

### Restaurant
| ID | Name | Location |
|---|---|---|
| 1 | Pastry | Jakarta, Indonesia |

### Menu Items (Restaurant ID: 1)
| ID | Name | Price | Description |
|----|------|-------|---|
| 1 | Chocolate Croissant | Rp 35,000 | Delicious chocolate filled croissant |
| 2 | Strawberry Tart | Rp 45,000 | Fresh strawberry tart with cream |
| 3 | Vanilla Donut | Rp 25,000 | Soft vanilla donut with glaze |
| 4 | Matcha Cake | Rp 55,000 | Premium matcha cake |

## 📡 Service-to-Service Communication

### Consumer-Provider Pattern

**Order Service (Consumer)** validates data from:
- **Customer Service**: Validates customer_id exists
- **Menu Service**: Validates menu items in order
- **Restaurant Service**: (Optional) Validate restaurant info

When creating an order, the Order Service makes HTTP requests to validate all referenced entities before persisting to database.

## 🗄️ Database Schema

### Customers Table
```sql
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

### Restaurants Table
```sql
CREATE TABLE restaurants (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

### Menu Items Table
```sql
CREATE TABLE menu_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    restaurant_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id) ON DELETE CASCADE
)
```

### Orders Table
```sql
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    customer_username VARCHAR(255) NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    customer_email VARCHAR(255) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    delivery_address VARCHAR(255) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    tax DECIMAL(10, 2) NOT NULL,
    status ENUM('on_process', 'on_delivery', 'delivered') DEFAULT 'on_process',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
)
```

### Order Items Table
```sql
CREATE TABLE order_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    menu_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (menu_id) REFERENCES menu_items(id) ON DELETE CASCADE
)
```

## 🧪 Testing with Postman

### Import Collection
1. Open Postman
2. Click **"Import"** → **"Upload Files"**
3. Select `documentation/Pastry_API.postman_collection.json`
4. Set environment variables:
   - `baseUrl` = `http://localhost:5000/api`
   - `token` = (obtained from login request)

### Test Workflow
1. Login → Get token
2. Get all menus
3. Create order
4. Get orders
5. Update order status
6. Get order details

## 🔐 Security Considerations

### JWT Tokens
- Tokens include role claims
- Role-based access control (RBAC) enforced at API Gateway
- Admin-only endpoints return 403 Forbidden for non-admin users

### Database
- Use environment variables for credentials (never hardcode)
- Implement input validation on all endpoints
- Use parameterized queries to prevent SQL injection

### CORS
- Only allow requests from trusted domains in production
- Currently allows all origins for development

## 🐛 Troubleshooting

### Common Issues

**1. "Database connection failed"**
- Check MySQL is running: `mysql -u root -p`
- Verify `.env` file has correct credentials
- Run `python backend/init_db.py` to create database

**2. "Port already in use"**
- Change port in `.env` file
- Or kill existing process: `lsof -i :5000`

**3. "CORS error"**
- Ensure all microservices are running
- Check `flask-cors` is installed

**4. "JWT token expired"**
- Tokens are set to expire (can be configured in `app.py`)
- Login again to get new token

**5. "Order validation failed"**
- Ensure Order Service can reach other services
- Check all service URLs in `.env`

## 📈 Performance Optimization

### Implemented
- Local caching of menu items in frontend
- Auto-refresh throttling (10-second intervals)
- Efficient database queries with proper indexing
- Lazy loading of order details

### Future Improvements
- Implement Redis caching for frequently accessed data
- Add pagination to orders table
- Optimize database queries with proper joins
- Implement request rate limiting

## 📝 Notes

- All prices are in Indonesian Rupiah (Rp)
- Tax is fixed at 5%
- Admin credentials should be changed in production
- JWT secret key should be changed in production
- Database connection pooling recommended for production
- Add HTTPS in production environment

## 🤝 Contributing

To contribute to this project:
1. Create a feature branch
2. Make your changes
3. Submit a pull request

## 📄 License

This project is for educational purposes.

## 👨‍💻 Support

For issues or questions:
1. Check the troubleshooting section
2. Review API documentation in Postman
3. Check browser console for JavaScript errors
4. Check terminal output for backend errors

---

**Version**: 1.0.0  
**Last Updated**: November 2025  
**Status**: ✅ Production Ready
