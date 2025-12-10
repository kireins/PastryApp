# 📡 API Endpoints Documentation

Dokumentasi lengkap semua endpoint Pastry Delivery System API.

**Base URL:** `http://localhost:5050/api`

**Authentication:** JWT Bearer Token (kecuali endpoint login)

---

## 🔐 Authentication

### POST /api/login

Login untuk mendapatkan JWT token. **Server menentukan role user berdasarkan username, bukan dari request client.**

**Request:**
```json
{
  "username": "customer",
  "password": "iamcustomer"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "Bearer",
  "expires_in": 86400,
  "expires_at": "2024-01-02T12:00:00.000000",
  "username": "customer",
  "role": "customer",
  "message": "Successfully logged in as customer"
}
```

**Error (400 Bad Request):**
```json
{
  "error": "Username and password are required"
}
```

**Error (401 Unauthorized):**
```json
{
  "error": "Invalid credentials"
}
```

**Credentials:**
- Customer: `username: customer`, `password: iamcustomer`
- Admin: `username: admin`, `password: iamadmin`

**Catatan Keamanan:**
- ✅ Role ditentukan oleh server berdasarkan username, bukan dari request client
- ✅ Token menggunakan format Bearer token
- ✅ Token memiliki expiration time (24 jam)
- ✅ Gunakan `Authorization: Bearer <token>` pada request berikutnya

---

## 👥 Customers

### GET /api/customers

Get all customers (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "081234567890",
    "created_at": "2025-11-14T10:00:00"
  }
]
```

### GET /api/customers/{id}

Get specific customer.

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "081234567890",
  "created_at": "2025-11-14T10:00:00"
}
```

### POST /api/customers

Create new customer (No auth required).

**Request:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "phone": "081234567890"
}
```

**Response (201 Created):**
```json
{
  "id": 3,
  "message": "Customer created successfully"
}
```

### PUT /api/customers/{id}

Update customer (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

**Request:**
```json
{
  "name": "John Updated",
  "email": "john.updated@example.com",
  "phone": "081234567891"
}
```

**Response (200 OK):**
```json
{
  "message": "Customer updated successfully"
}
```

### DELETE /api/customers/{id}

Delete customer (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

**Response (200 OK):**
```json
{
  "message": "Customer deleted successfully"
}
```

---

## 🏪 Restaurants

### GET /api/restaurants

Get all restaurants (No auth required).

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Pastry",
    "location": "Jakarta, Indonesia",
    "created_at": "2025-11-14T10:00:00"
  }
]
```

### GET /api/restaurants/{id}

Get specific restaurant (No auth required).

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "Pastry",
  "location": "Jakarta, Indonesia",
  "created_at": "2025-11-14T10:00:00"
}
```

### POST /api/restaurants

Create restaurant (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

**Request:**
```json
{
  "name": "New Restaurant",
  "location": "Bandung, Indonesia"
}
```

**Response (201 Created):**
```json
{
  "id": 2,
  "message": "Restaurant created successfully"
}
```

### PUT /api/restaurants/{id}

Update restaurant (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

**Request:**
```json
{
  "name": "Updated Restaurant",
  "location": "Surabaya, Indonesia"
}
```

### DELETE /api/restaurants/{id}

Delete restaurant (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

---

## 🍰 Menu Items

### GET /api/menus

Get all menu items (No auth required).

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "restaurant_id": 1,
    "name": "Chocolate Croissant",
    "price": 35000,
    "description": "Delicious chocolate filled croissant",
    "created_at": "2025-11-14T10:00:00"
  }
]
```

### GET /api/menus/{id}

Get specific menu item (No auth required).

**Response (200 OK):**
```json
{
  "id": 1,
  "restaurant_id": 1,
  "name": "Chocolate Croissant",
  "price": 35000,
  "description": "Delicious chocolate filled croissant",
  "created_at": "2025-11-14T10:00:00"
}
```

### GET /api/restaurants/{id}/menus

Get menu items for specific restaurant (No auth required).

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "restaurant_id": 1,
    "name": "Chocolate Croissant",
    "price": 35000,
    "description": "Delicious chocolate filled croissant"
  }
]
```

### POST /api/menus

Create menu item (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

**Request:**
```json
{
  "restaurant_id": 1,
  "name": "New Pastry",
  "price": 40000,
  "description": "Delicious new pastry"
}
```

**Response (201 Created):**
```json
{
  "id": 5,
  "message": "Menu item created successfully"
}
```

### PUT /api/menus/{id}

Update menu item (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

**Request:**
```json
{
  "name": "Updated Pastry",
  "price": 45000,
  "description": "Updated description"
}
```

### DELETE /api/menus/{id}

Delete menu item (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

---

## 📦 Orders

### GET /api/orders

Get orders (filtered by role).

**Headers:**
```
Authorization: Bearer <token>
```

**Query Parameters:**
- Admin: Returns all orders
- Customer: Returns only their orders

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "customer_id": 1,
    "customer_username": "customer",
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "customer_phone": "081234567890",
    "delivery_address": "Jl. Merdeka No. 123",
    "payment_method": "cash",
    "total_price": 36750,
    "tax": 1750,
    "status": "on_process",
    "created_at": "2025-11-14T10:00:00",
    "items": [
      {
        "menu_id": 1,
        "quantity": 1,
        "price": 35000,
        "menu_name": "Chocolate Croissant"
      }
    ]
  }
]
```

### GET /api/orders/{id}

Get specific order with items.

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "id": 1,
  "customer_id": 1,
  "customer_name": "John Doe",
  "delivery_address": "Jl. Merdeka No. 123",
  "total_price": 36750,
  "tax": 1750,
  "status": "on_process",
  "items": [
    {
      "menu_id": 1,
      "quantity": 1,
      "price": 35000,
      "menu_name": "Chocolate Croissant"
    }
  ]
}
```

### POST /api/orders

Create new order.

**Headers:**
```
Authorization: Bearer <customer_token>
```

**Request:**
```json
{
  "customer_id": 1,
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "customer_phone": "081234567890",
  "delivery_address": "Jl. Merdeka No. 123",
  "payment_method": "cash",
  "total_price": 36750,
  "tax": 1750,
  "items": [
    {
      "menu_id": 1,
      "quantity": 1,
      "price": 35000
    }
  ]
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "message": "Order created successfully",
  "status": "on_process"
}
```

### PATCH /api/orders/{id}/status

Update order status (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

**Request:**
```json
{
  "status": "on_delivery"
}
```

**Valid statuses:** `on_process`, `on_delivery`, `delivered`

**Response (200 OK):**
```json
{
  "message": "Order status updated successfully",
  "status": "on_delivery"
}
```

### DELETE /api/orders/{id}

Delete order (Admin only).

**Headers:**
```
Authorization: Bearer <admin_token>
```

**Response (200 OK):**
```json
{
  "message": "Order deleted successfully"
}
```

---

## 🔍 Error Responses

### 400 Bad Request
```json
{
  "error": "No data provided"
}
```

### 401 Unauthorized
```json
{
  "error": "Authorization token is missing. Please login first."
}
```

### 403 Forbidden
```json
{
  "error": "Unauthorized"
}
```

### 404 Not Found
```json
{
  "error": "Order not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Database connection failed"
}
```

---

## 📝 Notes

- Semua endpoint melalui API Gateway (port 5050)
- JWT token berlaku 24 jam
- Price dalam format integer (Rupiah, tanpa desimal)
- Status order: `on_process` → `on_delivery` → `delivered`

