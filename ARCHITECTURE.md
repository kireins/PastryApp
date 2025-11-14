# 📁 Project Structure Overview

## Complete Directory Layout

```
PastryApp/
│
├── README.md                           # Main documentation
├── QUICKSTART.md                       # Quick start guide
│
├── backend/                            # Backend microservices
│   ├── .env                            # Environment configuration
│   ├── requirements.txt                # Python dependencies
│   ├── init_db.py                      # Database initialization script
│   │
│   ├── api_gateway/
│   │   └── app.py                      # API Gateway (Port 5000)
│   │       ├── Login endpoint
│   │       ├── Route forwarding
│   │       └── JWT authentication
│   │
│   └── services/
│       ├── customer_service/
│       │   └── app.py                  # Port 5001
│       │       ├── GET /customers
│       │       ├── POST /customers
│       │       ├── PUT /customers/<id>
│       │       └── DELETE /customers/<id>
│       │
│       ├── restaurant_service/
│       │   └── app.py                  # Port 5002
│       │       ├── GET /restaurants
│       │       ├── POST /restaurants
│       │       ├── PUT /restaurants/<id>
│       │       └── DELETE /restaurants/<id>
│       │
│       ├── menu_service/
│       │   └── app.py                  # Port 5003
│       │       ├── GET /menus
│       │       ├── GET /restaurants/<id>/menus
│       │       ├── POST /menus
│       │       ├── PUT /menus/<id>
│       │       └── DELETE /menus/<id>
│       │
│       └── order_service/
│           └── app.py                  # Port 5004 (Consumer)
│               ├── GET /orders
│               ├── POST /orders (validates with other services)
│               ├── PATCH /orders/<id>/status
│               ├── DELETE /orders/<id>
│               └── Service validation logic
│
├── frontend/                           # Client-side applications
│   ├── index.html                      # Customer interface
│   │   ├── Login modal
│   │   ├── Hero section
│   │   ├── Menu grid (4 items)
│   │   ├── Cart sidebar
│   │   ├── Delivery form
│   │   ├── Receipt modal
│   │   ├── Orders history
│   │   └── Animations & styling
│   │
│   └── admin.html                      # Admin dashboard
│       ├── Navigation bar
│       ├── Sidebar navigation
│       ├── Statistics cards (4 metrics)
│       ├── Filter & search section
│       ├── Orders management table
│       ├── Order details modal
│       ├── Status dropdown menu
│       └── Animations & styling
│
└── documentation/
    └── Pastry_API.postman_collection.json  # Postman collection
        ├── Authentication endpoints
        ├── Customer endpoints
        ├── Restaurant endpoints
        ├── Menu endpoints
        └── Order endpoints
```

## 🔄 Service Communication Flow

```
┌─────────────────────────────────────────┐
│         Frontend (Browser)              │
│  index.html (Customer) / admin.html     │
└────────────────┬────────────────────────┘
                 │ HTTP Requests
                 ↓
┌─────────────────────────────────────────┐
│      API Gateway (Port 5000)            │
│  - JWT Authentication                   │
│  - Route Forwarding                     │
│  - Role-Based Access Control            │
└──┬──────┬──────────┬──────────┬─────────┘
   │      │          │          │
   ↓      ↓          ↓          ↓
┌──────┐┌────────┐┌──────┐┌────────┐
│Cust. ││Restau.││Menu  ││Order   │
│Srv.  ││ Srv.  ││ Srv. ││ Srv.   │
│5001  ││ 5002  ││ 5003 ││ 5004   │
└──────┘└────────┘└──────┘└────────┘
   │      │          │          │
   └──────┴──────────┴──────────┴─── MySQL Database
                                      (pastry_db)
```

## 📊 Database Schema

```
CUSTOMERS
├── id (PK)
├── name
├── email
├── phone
└── created_at

RESTAURANTS
├── id (PK)
├── name
├── location
└── created_at

MENU_ITEMS
├── id (PK)
├── restaurant_id (FK)
├── name
├── price
├── description
└── created_at

ORDERS
├── id (PK)
├── customer_id (FK)
├── customer_username
├── customer_name
├── customer_email
├── customer_phone
├── delivery_address
├── payment_method
├── total_price
├── tax
├── status (on_process, on_delivery, delivered)
├── created_at
└── updated_at

ORDER_ITEMS
├── id (PK)
├── order_id (FK)
├── menu_id (FK)
├── quantity
├── price
└── created_at
```

## 🔗 API Endpoints Summary

### Authentication (API Gateway)
```
POST /api/login
  - Customer & Admin login
  - Returns JWT token with role
```

### Customers (Port 5001)
```
GET    /api/customers                (Admin only)
GET    /api/customers/<id>
POST   /api/customers
PUT    /api/customers/<id>
DELETE /api/customers/<id>           (Admin only)
```

### Restaurants (Port 5002)
```
GET    /api/restaurants
GET    /api/restaurants/<id>
POST   /api/restaurants              (Admin only)
PUT    /api/restaurants/<id>         (Admin only)
DELETE /api/restaurants/<id>         (Admin only)
```

### Menu (Port 5003)
```
GET    /api/menus
GET    /api/menus/<id>
GET    /api/restaurants/<id>/menus
POST   /api/menus                    (Admin only)
PUT    /api/menus/<id>               (Admin only)
DELETE /api/menus/<id>               (Admin only)
```

### Orders (Port 5004)
```
GET    /api/orders                   (Role-filtered)
GET    /api/orders/<id>
POST   /api/orders                   (Validates with other services)
PUT    /api/orders/<id>
PATCH  /api/orders/<id>/status       (Admin only)
DELETE /api/orders/<id>              (Admin only)
```

## 🎨 Frontend Structure

### Customer Interface (index.html)

```html
<nav>
  - Brand
  - Login/User Info
  - Logout

<hero-section>
  - Title
  - Description
  - CTA Button

<menu-section>
  - Menu Grid (4 responsive cards)
  - Cart Sidebar (sticky)
    - Items list
    - Cart summary
  - Delivery Form
    - Name, Email, Phone, Address
    - Payment method
    - Submit button
  - Orders History Section
    - Order cards with status

<receipt-modal>
  - Order confirmation
  - Items breakdown
  - Receipt footer
```

### Admin Dashboard (admin.html)

```html
<nav>
  - Brand
  - Admin Title
  - Admin Name
  - Logout

<sidebar>
  - Navigation links
  - Active indicator

<main-content>
  <dashboard-header>
    - Title
    - Subtitle

  <statistics-section>
    - Total Orders
    - On Process
    - On Delivery
    - Delivered
    - Quick insights

  <filters-section>
    - Search by Order ID
    - Filter by Status
    - Refresh button

  <orders-table>
    - Order ID
    - Customer
    - Items count
    - Total price
    - Status (dropdown)
    - Delivery address
    - View/Delete buttons

  <order-details-modal>
    - Order info
    - Customer info
    - Items list
    - Payment info
```

## 🎨 Animation Types

### Applied Throughout
1. **slideDown** - Navigation entrance
2. **slideInLeft** - Content from left
3. **slideInRight** - Content from right
4. **slideInUp** - Content from bottom
5. **cardAppear** - Card entrance with y-offset
6. **scaleUp** - Title scaling
7. **fadeIn** - Modal background
8. **pulse** - Order status indicator
9. **spin** - Loading spinner
10. **rowAppear** - Table rows animation

## 🔐 Security Implementation

### JWT Authentication
- Generated in API Gateway
- Contains: username, role
- Verified on protected endpoints
- RBAC enforced at gateway level

### Role-Based Access Control
- **Customer**: Read menus, place orders, view own orders
- **Admin**: Full CRUD on all resources, order status updates

### CORS Configuration
- Enabled for local development
- Should be restricted in production

## 📦 Dependencies

### Backend
```
Flask==3.0.0
Flask-JWT-Extended==4.5.3
Flask-CORS==4.0.0
requests==2.31.0
python-dotenv==1.0.0
mysql-connector-python==8.2.0
PyMySQL==1.1.0
```

### Frontend
- Pure HTML/CSS/JavaScript
- No external dependencies
- Fetch API for HTTP requests
- LocalStorage for session persistence

## 🚀 Deployment Checklist

- [ ] Change JWT secret key in `.env`
- [ ] Update database credentials
- [ ] Set FLASK_ENV=production
- [ ] Enable HTTPS
- [ ] Configure CORS for production domain
- [ ] Set up database backups
- [ ] Enable request rate limiting
- [ ] Add input validation sanitization
- [ ] Implement error logging
- [ ] Set up monitoring & alerts

## 📝 Configuration Files

### .env
```
FLASK_ENV=development
JWT_SECRET_KEY=your_secret
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DATABASE=pastry_db
[All service ports and URLs]
```

### requirements.txt
```
All Python dependencies
Version pinned for reproducibility
```

### Postman Collection
```json
- All endpoints
- Request templates
- Environment variables
- Sample data
```

## 🔄 Data Flow Examples

### Order Creation Flow
1. Customer fills form
2. Frontend calls POST /api/orders
3. API Gateway validates JWT
4. Order Service receives request
5. Order Service validates customer (→ Customer Service)
6. Order Service validates items (→ Menu Service)
7. Order persisted to database
8. Frontend receives order ID
9. Receipt modal displays

### Order Status Update Flow
1. Admin clicks status badge
2. Dropdown shows options
3. Admin selects new status
4. Frontend calls PATCH /api/orders/<id>/status
5. API Gateway checks admin role
6. Order Service updates status
7. Table auto-refreshes (10s interval)
8. Status displays with animation

---

This structure demonstrates a professional microservices architecture with proper separation of concerns, scalability, and maintainability.
