# 📝 API Request/Response Examples

Contoh lengkap request dan response untuk setiap endpoint kunci.

---

## 🔐 Authentication Examples

### Example 1: Customer Login

**Request:**
```http
POST http://localhost:5050/api/login
Content-Type: application/json

{
  "username": "customer",
  "password": "iamcustomer"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwMDAwMDAwMCwianRpIjoiMTIzNDU2IiwidHlwIjoiYWNjZXNzIiwic3ViIjoiY3VzdG9tZXIiLCJuYmYiOjE3MDAwMDAwMDAsImV4cCI6MTcwMDA4NjQwMCwicm9sZSI6ImN1c3RvbWVyIn0.abc123",
  "token_type": "Bearer",
  "expires_in": 86400,
  "expires_at": "2024-01-02T12:00:00.000000",
  "username": "customer",
  "role": "customer",
  "message": "Successfully logged in as customer"
}
```

**Catatan:** Role ditentukan oleh server berdasarkan username, bukan dari request client.

### Example 2: Admin Login

**Request:**
```http
POST http://localhost:5050/api/login
Content-Type: application/json

{
  "username": "admin",
  "password": "iamadmin"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "Bearer",
  "expires_in": 86400,
  "expires_at": "2024-01-02T12:00:00.000000",
  "username": "admin",
  "role": "admin",
  "message": "Successfully logged in as admin"
}
```

---

## 🍰 Menu Examples

### Example 3: Get All Menus

**Request:**
```http
GET http://localhost:5050/api/menus
```

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
  },
  {
    "id": 2,
    "restaurant_id": 1,
    "name": "Strawberry Tart",
    "price": 45000,
    "description": "Fresh strawberry tart with cream",
    "created_at": "2025-11-14T10:00:00"
  },
  {
    "id": 3,
    "restaurant_id": 1,
    "name": "Vanilla Donut",
    "price": 25000,
    "description": "Soft vanilla donut with glaze",
    "created_at": "2025-11-14T10:00:00"
  },
  {
    "id": 4,
    "restaurant_id": 1,
    "name": "Matcha Cake",
    "price": 55000,
    "description": "Premium matcha cake",
    "created_at": "2025-11-14T10:00:00"
  }
]
```

### Example 4: Get Specific Menu

**Request:**
```http
GET http://localhost:5050/api/menus/1
```

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

---

## 👥 Customer Examples

### Example 5: Create Customer

**Request:**
```http
POST http://localhost:5050/api/customers
Content-Type: application/json

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

---

## 📦 Order Examples

### Example 6: Create Order

**Request:**
```http
POST http://localhost:5050/api/orders
Content-Type: application/json
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...

{
  "customer_id": 1,
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "customer_phone": "081234567890",
  "delivery_address": "Jl. Merdeka No. 123, Jakarta",
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

### Example 7: Get Orders (Customer)

**Request:**
```http
GET http://localhost:5050/api/orders
Authorization: Bearer <customer_token>
```

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

### Example 8: Get Orders (Admin)

**Request:**
```http
GET http://localhost:5050/api/orders
Authorization: Bearer <admin_token>
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "customer_id": 1,
    "customer_name": "John Doe",
    "total_price": 36750,
    "status": "on_process",
    "items": [
      {
        "menu_id": 1,
        "quantity": 1,
        "price": 35000,
        "menu_name": "Chocolate Croissant"
      }
    ]
  },
  {
    "id": 2,
    "customer_id": 2,
    "customer_name": "Jane Smith",
    "total_price": 47250,
    "status": "on_delivery",
    "items": [
      {
        "menu_id": 2,
        "quantity": 1,
        "price": 45000,
        "menu_name": "Strawberry Tart"
      }
    ]
  }
]
```

### Example 9: Update Order Status

**Request:**
```http
PATCH http://localhost:5050/api/orders/1/status
Content-Type: application/json
Authorization: Bearer <admin_token>

{
  "status": "on_delivery"
}
```

**Response (200 OK):**
```json
{
  "message": "Order status updated successfully",
  "status": "on_delivery"
}
```

### Example 10: Get Order Details

**Request:**
```http
GET http://localhost:5050/api/orders/1
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "id": 1,
  "customer_id": 1,
  "customer_username": "customer",
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "customer_phone": "081234567890",
  "delivery_address": "Jl. Merdeka No. 123, Jakarta",
  "payment_method": "cash",
  "total_price": 36750,
  "tax": 1750,
  "status": "on_process",
  "created_at": "2025-11-14T10:00:00",
  "updated_at": "2025-11-14T10:00:00",
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

---

## ❌ Error Examples

### Example 11: Unauthorized (No Token)

**Request:**
```http
GET http://localhost:5050/api/orders
```

**Response (401 Unauthorized):**
```json
{
  "error": "Authorization token is missing. Please login first."
}
```

### Example 12: Invalid Credentials

**Request:**
```http
POST http://localhost:5050/api/login
Content-Type: application/json

{
  "username": "wrong",
  "password": "wrong",
  "role": "customer"
}
```

**Response (401 Unauthorized):**
```json
{
  "error": "Invalid credentials"
}
```

### Example 13: Order Not Found

**Request:**
```http
GET http://localhost:5050/api/orders/999
Authorization: Bearer <token>
```

**Response (404 Not Found):**
```json
{
  "error": "Order not found"
}
```

### Example 14: Forbidden (Wrong Role)

**Request:**
```http
DELETE http://localhost:5050/api/orders/1
Authorization: Bearer <customer_token>
```

**Response (403 Forbidden):**
```json
{
  "error": "Unauthorized"
}
```

---

## 🔄 Complete Workflow Example

### Step 1: Login
```http
POST /api/login
→ Get token
```

### Step 2: Get Menus
```http
GET /api/menus
→ See available items
```

### Step 3: Create Customer
```http
POST /api/customers
→ Get customer_id
```

### Step 4: Create Order
```http
POST /api/orders
Authorization: Bearer <token>
→ Order created
```

### Step 5: View Orders
```http
GET /api/orders
Authorization: Bearer <token>
→ See order history
```

### Step 6: Update Status (Admin)
```http
PATCH /api/orders/1/status
Authorization: Bearer <admin_token>
→ Status updated
```

---

## 📝 Notes

- Semua request ke API Gateway (port 5050)
- Token harus disertakan di header `Authorization: Bearer <token>`
- Price dalam format integer (Rupiah)
- Timestamp dalam format ISO 8601

