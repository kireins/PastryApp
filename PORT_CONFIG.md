# 🔌 Port Configuration Summary

## Current Port Setup

**API Gateway**: `http://localhost:5050/api` ✅
- **Why 5050?** Port 5000 is reserved by macOS AirPlay Receiver
- **What it does**: Central authentication gateway, routes requests to microservices

**Microservices** (Behind the API Gateway):
- Customer Service: `http://localhost:5001` (internal)
- Menu Service: `http://localhost:5003` (internal)  
- Order Service: `http://localhost:5004` (internal)

**Frontend**: `http://localhost:8000` ✅
- Customer Interface: http://localhost:8000/index.html
- Admin Dashboard: http://localhost:8000/admin.html

---

## Why NOT Port 5000?

```bash
# If you try to use port 5000:
lsof -i :5000

# You'll see:
COMMAND     PID    USER   FD   TYPE   DEVICE SIZE NODE NAME
ControlCe  93064   user   10u  IPv4   ...    TCP *:commplex-main (LISTEN)
```

This is macOS's **AirPlay Receiver** service running on port 5000. To use port 5000, you'd need to disable AirPlay in System Preferences.

---

## How to Use Postman

### Step 1: Import the Collection
1. Open Postman
2. Click **Import**
3. Select: `/Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/documentation/Pastry_API.postman_collection.json`

### Step 2: Update Base URL (Already Done ✅)
The collection now has `baseUrl` set to: `http://localhost:5050/api`

### Step 3: Login First
1. Go to **Authentication** → **Login - Customer** (or Login - Admin)
2. Click **Send**
3. You'll get a response with an `access_token`
4. Copy the token value

### Step 4: Set Token in Postman
1. Click **Collections** → Select variable tab
2. Find `token` variable
3. Paste your token in the Current Value field
4. Click **Save**

### Step 5: Test Endpoints
Now you can test any endpoint in the collection!

---

## Quick Test Commands

### Login (Get Token)
```bash
curl -X POST http://localhost:5050/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"customer","password":"iamcustomer","role":"customer"}'
```

Response:
```json
{
  "access_token": "eyJhbGc... (very long token)",
  "user": {
    "id": 1,
    "username": "customer",
    "role": "customer"
  }
}
```

### Get Menus (No Auth Required)
```bash
curl http://localhost:5050/api/menus
```

### Get Orders (Auth Required)
```bash
curl -X GET http://localhost:5050/api/orders \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────┐
│         Frontend (Port 8000)            │
│  ┌──────────────┬─────────────────────┐ │
│  │ index.html   │   admin.html        │ │
│  │ (Customer)   │   (Admin)           │ │
│  └──────────┬───┴──────────────┬──────┘ │
└─────────────┼──────────────────┼────────┘
              │ HTTP Requests    │
              ▼                  ▼
    ┌───────────────────────────────────┐
    │   API Gateway (Port 5050)         │
    │   ├─ JWT Authentication           │
    │   ├─ Role-Based Access Control    │
    │   └─ Request Routing              │
    └─┬────────────┬─────────┬─────────┬┘
      │            │         │         │
      ▼            ▼         ▼         ▼
   PORT 5001   PORT 5003  PORT 5004   (More)
   Customer    Menu      Order       Services
   Service     Service   Service
```

---

## Available Endpoints

### Authentication
- `POST /login` - Login with username, password, and role

### Customers
- `GET /customers` - Get all customers
- `GET /customers/{id}` - Get customer by ID
- `POST /customers` - Create new customer
- `PUT /customers/{id}` - Update customer
- `DELETE /customers/{id}` - Delete customer

### Menu Items
- `GET /menus` - Get all menu items
- `GET /menus/{id}` - Get menu item by ID
- `GET /restaurants/{id}/menus` - Get menus for a restaurant
- `POST /menus` - Create menu item
- `PUT /menus/{id}` - Update menu item

### Orders
- `GET /orders` - Get all orders
- `GET /orders/{id}` - Get order by ID
- `POST /orders` - Create new order
- `PATCH /orders/{id}/status` - Update order status
- `DELETE /orders/{id}` - Delete order

### Restaurants
- `GET /restaurants` - Get all restaurants
- `GET /restaurants/{id}` - Get restaurant by ID
- `POST /restaurants` - Create restaurant
- `PUT /restaurants/{id}` - Update restaurant

---

## Test Credentials

| Role | Username | Password |
|------|----------|----------|
| Customer | `customer` | `iamcustomer` |
| Admin | `admin` | `iamadmin` |

---

## Sample Data (Pre-loaded)

### Customers
- ID 1: John Doe (customer)
- ID 2: Kirei Najwa Shafira (customer)

### Restaurants
- ID 1: Pastry Paradise

### Menu Items
- ID 1: Chocolate Croissant - Rp 35,000
- ID 2: Strawberry Tart - Rp 45,000
- ID 3: Vanilla Cheesecake - Rp 50,000
- ID 4: Blueberry Muffin - Rp 40,000

### Orders
- ID 1: Status "on_process" - 1 item(s) - Rp 36,750

---

## Troubleshooting

### "Port Already In Use"
```bash
# Find what's using the port
lsof -i :5050

# Kill it (if it's an old service)
kill -9 <PID>
```

### "Connection Refused"
Make sure services are running:
```bash
netstat -an | grep -E '5050|5001|5003|5004|8000' | grep LISTEN
```

Should show 5 lines (all ports LISTEN).

### "Unauthorized" in Postman
1. Make sure you logged in and got the token
2. Set the token in the collection variables
3. Try logging in again if token expired

### Backend Not Responding
Start all services:
```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp
chmod +x STARTUP.sh
./STARTUP.sh
```

---

## Files Updated

✅ `.env` - API_GATEWAY_PORT changed from 5000 to 5050
✅ `frontend/index.html` - API_URL changed to port 5050
✅ `frontend/admin.html` - API_URL changed to port 5050
✅ `documentation/Pastry_API.postman_collection.json` - baseUrl changed to port 5050

---

**Summary**: Use **port 5050** for all API calls instead of 5000! 🎉
