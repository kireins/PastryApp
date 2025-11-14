# 📋 File Directory & Purpose Guide

## Complete File Listing with Descriptions

### Root Documentation Files

#### `README.md` (Main Documentation)
- **Purpose**: Complete project documentation
- **Contents**: 
  - Feature overview
  - Technology stack
  - Installation instructions
  - Usage guide (customer & admin)
  - Default data
  - API endpoints
  - Database schema
  - Key concepts explained
  - Troubleshooting guide
- **Audience**: Everyone (comprehensive reference)
- **Size**: 2000+ lines

#### `QUICKSTART.md` (Quick Setup Guide)
- **Purpose**: Get running in 5 minutes
- **Contents**:
  - Quick setup steps
  - Terminal commands for all services
  - Default credentials
  - Quick test workflow
  - Common issues & fixes
- **Audience**: New users wanting to test quickly
- **Size**: 300+ lines

#### `ARCHITECTURE.md` (System Design)
- **Purpose**: Understand the architecture
- **Contents**:
  - Complete directory structure
  - Service communication flow
  - Database schema detailed view
  - API endpoints grouped by service
  - Animation types reference
  - Security implementation details
  - Data flow examples
- **Audience**: Developers, architects
- **Size**: 400+ lines

#### `INSTALLATION.md` (Detailed Setup)
- **Purpose**: Step-by-step installation guide
- **Contents**:
  - System requirements
  - Python/MySQL installation (Mac/Linux/Windows)
  - Virtual environment setup
  - Dependency installation
  - Environment configuration
  - Database initialization
  - Service startup
  - Troubleshooting
  - Production deployment
  - Security hardening
- **Audience**: System administrators, developers
- **Size**: 500+ lines

#### `COMPLETION_SUMMARY.md` (Project Summary)
- **Purpose**: Overview of what was delivered
- **Contents**:
  - All components included
  - Features implemented
  - Design specifications
  - Quick start summary
  - Learning outcomes
- **Audience**: Project stakeholders
- **Size**: 300+ lines

---

## Backend Files

### `backend/.env` (Environment Configuration)
- **Purpose**: Configuration for all services
- **Format**: Key=Value pairs
- **Contains**:
  - Flask environment settings
  - JWT configuration
  - Service ports (5000-5004)
  - Service URLs
  - MySQL credentials
  - Database name
- **Edit this to**: Change ports, credentials, environment
- **Never commit**: This file (add to .gitignore)

### `backend/requirements.txt` (Python Dependencies)
- **Purpose**: List all required Python packages
- **Format**: Package==Version
- **Contains**:
  - Flask 3.0.0
  - Flask-JWT-Extended 4.5.3
  - Flask-CORS 4.0.0
  - requests 2.31.0
  - python-dotenv 1.0.0
  - mysql-connector-python 8.2.0
  - PyMySQL 1.1.0
- **Usage**: `pip install -r requirements.txt`

### `backend/init_db.py` (Database Initialization)
- **Purpose**: Create database, tables, and sample data
- **Functions**:
  - `create_database_and_tables()` - Creates schema
  - `insert_sample_data()` - Adds test data
- **Usage**: `python init_db.py`
- **Creates**:
  - pastry_db database
  - 5 tables with relationships
  - 2 customers, 1 restaurant, 4 menu items
- **Safe**: Won't duplicate if run multiple times

---

## API Gateway

### `backend/api_gateway/app.py` (Main Gateway)
- **Purpose**: Central routing and authentication
- **Port**: 5000
- **Key Features**:
  - POST /api/login - JWT token generation
  - GET/POST/PUT/DELETE routes for all services
  - JWT verification on protected endpoints
  - Role-based access control (RBAC)
  - CORS enabled
- **Forwards to**:
  - Customer Service (5001)
  - Restaurant Service (5002)
  - Menu Service (5003)
  - Order Service (5004)
- **Authorization**: Bearer token in Authorization header

---

## Microservices

### Customer Service

**File**: `backend/services/customer_service/app.py`
- **Port**: 5001
- **Role**: Provider
- **Endpoints**:
  - GET /customers - Get all
  - GET /customers/<id> - Get one
  - POST /customers - Create
  - PUT /customers/<id> - Update
  - DELETE /customers/<id> - Delete (admin only)
- **Database Table**: customers
- **Used By**: Order Service (validation)

### Restaurant Service

**File**: `backend/services/restaurant_service/app.py`
- **Port**: 5002
- **Role**: Provider
- **Endpoints**:
  - GET /restaurants - Get all
  - GET /restaurants/<id> - Get one
  - POST /restaurants - Create (admin only)
  - PUT /restaurants/<id> - Update (admin only)
  - DELETE /restaurants/<id> - Delete (admin only)
- **Database Table**: restaurants
- **Used By**: Menu Service (validation)

### Menu Service

**File**: `backend/services/menu_service/app.py`
- **Port**: 5003
- **Role**: Provider
- **Endpoints**:
  - GET /menus - Get all items
  - GET /menus/<id> - Get one item
  - GET /restaurants/<id>/menus - Get restaurant's menu
  - POST /menus - Create item (admin only)
  - PUT /menus/<id> - Update item (admin only)
  - DELETE /menus/<id> - Delete item (admin only)
- **Database Table**: menu_items
- **Used By**: Order Service (validation)

### Order Service

**File**: `backend/services/order_service/app.py`
- **Port**: 5004
- **Role**: Consumer (validates with other services)
- **Key Features**:
  - Validates customer exists (→ Customer Service)
  - Validates menu items exist (→ Menu Service)
  - Creates orders with items
- **Endpoints**:
  - GET /orders - Get orders (filtered by role)
  - GET /orders/<id> - Get with items
  - POST /orders - Create order (validates)
  - PUT /orders/<id> - Update order
  - PATCH /orders/<id>/status - Update status (admin only)
  - DELETE /orders/<id> - Delete order (admin only)
- **Database Tables**: orders, order_items

---

## Frontend Files

### `frontend/index.html` (Customer Interface)
- **Purpose**: Customer-facing application
- **Size**: ~1200 lines
- **Includes**:
  - HTML structure
  - CSS styling with animations
  - JavaScript functionality
  - No external dependencies
- **Features**:
  - Login modal
  - Hero section
  - Menu grid (4 items)
  - Cart sidebar
  - Delivery form
  - Receipt modal
  - Order history
- **Animations**: 10+ animation effects
- **Responsive**: Mobile & desktop
- **Storage**: Uses localStorage for sessions

### `frontend/admin.html` (Admin Dashboard)
- **Purpose**: Admin order management
- **Size**: ~1000 lines
- **Includes**:
  - HTML structure
  - CSS styling with animations
  - JavaScript functionality
  - No external dependencies
- **Features**:
  - Navigation bar
  - Sidebar menu
  - Statistics cards
  - Orders table
  - Search & filter
  - Status dropdown
  - Order details modal
- **Animations**: 10+ animation effects
- **Responsive**: Mobile & desktop
- **Auto-refresh**: Every 10 seconds

---

## Documentation Files

### `documentation/Pastry_API.postman_collection.json`
- **Purpose**: API testing and documentation
- **Format**: Postman Collection v2.1.0
- **Contents**:
  - Authentication endpoints
  - Customer CRUD endpoints
  - Restaurant CRUD endpoints
  - Menu item CRUD endpoints
  - Order management endpoints
  - Health check endpoint
- **Environment Variables**:
  - `baseUrl` - API Gateway URL
  - `token` - JWT token
- **Usage**: Import into Postman, test endpoints

---

## Database Files

### Database Schema (Created by `init_db.py`)

#### `customers` Table
```
id (INT, PK, AI)
name (VARCHAR 255, NOT NULL)
email (VARCHAR 255, UNIQUE, NOT NULL)
phone (VARCHAR 20, NOT NULL)
created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
```

#### `restaurants` Table
```
id (INT, PK, AI)
name (VARCHAR 255, NOT NULL)
location (VARCHAR 255, NOT NULL)
created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
```

#### `menu_items` Table
```
id (INT, PK, AI)
restaurant_id (INT, FK)
name (VARCHAR 255, NOT NULL)
price (DECIMAL 10,2, NOT NULL)
description (TEXT)
created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
```

#### `orders` Table
```
id (INT, PK, AI)
customer_id (INT, FK)
customer_username (VARCHAR 255, NOT NULL)
customer_name (VARCHAR 255, NOT NULL)
customer_email (VARCHAR 255, NOT NULL)
customer_phone (VARCHAR 20, NOT NULL)
delivery_address (VARCHAR 255, NOT NULL)
payment_method (VARCHAR 50, NOT NULL)
total_price (DECIMAL 10,2, NOT NULL)
tax (DECIMAL 10,2, NOT NULL)
status (ENUM, DEFAULT 'on_process')
created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
updated_at (TIMESTAMP, AUTO UPDATE)
```

#### `order_items` Table
```
id (INT, PK, AI)
order_id (INT, FK)
menu_id (INT, FK)
quantity (INT, NOT NULL)
price (DECIMAL 10,2, NOT NULL)
created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
```

---

## Configuration & Setup Files

### Virtual Environment Setup
- **Created**: `backend/venv/` (local only, don't commit)
- **Purpose**: Isolate Python dependencies
- **Setup**: `python3 -m venv venv`
- **Activate**: `source venv/bin/activate`

### Git Configuration (Recommended)
Create `.gitignore` file:
```
venv/
__pycache__/
*.pyc
.env
*.log
.DS_Store
```

---

## File Relationships & Dependencies

```
Frontend (Browser)
    ↓
API Gateway (app.py:5000)
    ├→ Customer Service (app.py:5001)
    ├→ Restaurant Service (app.py:5002)
    ├→ Menu Service (app.py:5003)
    └→ Order Service (app.py:5004)
    ↓
MySQL Database
    ├─ customers
    ├─ restaurants
    ├─ menu_items
    ├─ orders
    └─ order_items
```

---

## File Edit Guide

### What to Edit

1. **`.env`** - Change:
   - Ports if conflicts
   - MySQL credentials
   - JWT secret (production)

2. **`init_db.py`** - Add/modify:
   - Sample menu items
   - Additional customers
   - Restaurant data

3. **`frontend/index.html`** - Customize:
   - Colors (CSS variables)
   - Menu items display
   - Form fields

4. **`frontend/admin.html`** - Customize:
   - Dashboard layout
   - Statistics
   - Table columns

### What NOT to Edit

- Service API logic (unless adding features)
- Database schema (without migration planning)
- API Gateway routes (central routing)
- JWT middleware (security-critical)

---

## File Sizes Summary

| File | Type | Size |
|------|------|------|
| README.md | Docs | ~2000 lines |
| QUICKSTART.md | Docs | ~300 lines |
| ARCHITECTURE.md | Docs | ~400 lines |
| INSTALLATION.md | Docs | ~500 lines |
| api_gateway/app.py | Code | ~250 lines |
| customer_service/app.py | Code | ~150 lines |
| restaurant_service/app.py | Code | ~150 lines |
| menu_service/app.py | Code | ~180 lines |
| order_service/app.py | Code | ~250 lines |
| index.html | Frontend | ~1200 lines |
| admin.html | Frontend | ~1000 lines |
| init_db.py | Database | ~150 lines |
| Postman Collection | API Docs | ~400 lines |

**Total**: ~8000+ lines of code and documentation

---

## Access Paths

### Local Development
- Customer: http://localhost:8000/index.html
- Admin: http://localhost:8000/admin.html
- API Gateway: http://localhost:5000/api/

### Service URLs
- Customer Service: http://localhost:5001
- Restaurant Service: http://localhost:5002
- Menu Service: http://localhost:5003
- Order Service: http://localhost:5004

### Database
- Host: localhost
- Port: 3306
- Database: pastry_db
- User: root (default)

---

This file provides a complete reference for understanding the purpose and location of every file in the project.

