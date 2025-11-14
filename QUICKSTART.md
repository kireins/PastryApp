# 🚀 Quick Start Guide - Pastry Delivery System

Get up and running with the Pastry Delivery System in 5 minutes!

## ⚡ Quick Setup (Mac/Linux)

### 1. Create Virtual Environment

```bash
cd /path/to/PastryApp/backend
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize Database

Make sure MySQL is running, then:

```bash
python init_db.py
```

Expected output:
```
🔧 Creating database and tables...

Database 'pastry_db' created or already exists.
Customers table created or already exists.
Restaurants table created or already exists.
Menu items table created or already exists.
Orders table created or already exists.
Order items table created or already exists.

✅ All tables created successfully!

✅ Sample customers inserted.
✅ Sample restaurant inserted.
✅ Sample menu items inserted.

✅ Sample data inserted successfully!
```

### 4. Start All Services (5 Terminal Windows)

#### Terminal 1: API Gateway (Port 5000)
```bash
cd backend/api_gateway
python app.py
```
Output: `Running on http://0.0.0.0:5000`

#### Terminal 2: Customer Service (Port 5001)
```bash
cd backend/services/customer_service
python app.py
```
Output: `Running on http://0.0.0.0:5001`

#### Terminal 3: Restaurant Service (Port 5002)
```bash
cd backend/services/restaurant_service
python app.py
```
Output: `Running on http://0.0.0.0:5002`

#### Terminal 4: Menu Service (Port 5003)
```bash
cd backend/services/menu_service
python app.py
```
Output: `Running on http://0.0.0.0:5003`

#### Terminal 5: Order Service (Port 5004)
```bash
cd backend/services/order_service
python app.py
```
Output: `Running on http://0.0.0.0:5004`

### 5. Start Frontend Server

```bash
cd frontend
python3 -m http.server 8000
```

### 6. Access the Application

- **Customer**: Open browser to http://localhost:8000/index.html
- **Admin**: Open browser to http://localhost:8000/admin.html

## 🔐 Default Login Credentials

### Customer
- Username: `customer`
- Password: `iamcustomer`

### Admin
- Username: `admin`
- Password: `iamadmin`

## 🧪 Quick Test Workflow

### 1. Customer Flow
1. Go to http://localhost:8000/index.html
2. Click "Login"
3. Enter customer credentials
4. Browse menu items
5. Add items to cart
6. Fill delivery details
7. Place order
8. View receipt confirmation
9. See order in "Your Orders" section

### 2. Admin Flow
1. Go to http://localhost:8000/index.html
2. Click "Login"
3. Enter admin credentials
4. Automatically redirected to admin.html
5. View order statistics
6. Search/filter orders
7. Click status badge to change order status
8. Click "View" to see order details
9. Click "Delete" to remove orders

## 📊 API Testing with Curl

### Login
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"customer","password":"iamcustomer","role":"customer"}'
```

### Get Menus
```bash
curl http://localhost:5000/api/menus
```

### Create Order (requires token)
```bash
curl -X POST http://localhost:5000/api/orders \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id":1,
    "customer_name":"John Doe",
    "customer_email":"john@example.com",
    "customer_phone":"081234567890",
    "delivery_address":"Jl. Example",
    "payment_method":"cash",
    "total_price":115500,
    "tax":5500,
    "items":[{"menu_id":1,"quantity":2,"price":35000},{"menu_id":3,"quantity":1,"price":25000}]
  }'
```

## 🎨 Features You Can Try

### Customer
- ✅ Browse 4 menu items with animations
- ✅ Add/remove items from cart
- ✅ Real-time cart calculations
- ✅ Receipt-style order confirmation
- ✅ Track order status
- ✅ Auto-refresh orders (10 seconds)

### Admin
- ✅ View order statistics
- ✅ Filter orders by status
- ✅ Search orders by ID
- ✅ Update order status (on_process → on_delivery → delivered)
- ✅ View complete order details
- ✅ Delete orders
- ✅ Real-time dashboard updates

## 🐛 Troubleshooting

### "Address already in use"
Port 5000-5004 or 8000 already in use.
```bash
# Kill process on port (e.g., 5000)
lsof -i :5000  # Find process
kill -9 PID    # Kill it
```

### "Connection refused"
Services not running. Make sure all 5 services are started in separate terminals.

### "Database connection failed"
1. Check MySQL is running: `mysql -u root -p`
2. Verify `.env` credentials
3. Run `python init_db.py` again

### "CORS error" in browser
All services must be running. Check all 5 terminals.

### "Invalid token"
- Token may have expired, login again
- Copy full token including "Bearer " prefix in Postman

## 📈 Sample Data Available

### Menu Items (Ready to Order)
1. **Chocolate Croissant** - Rp 35,000
2. **Strawberry Tart** - Rp 45,000
3. **Vanilla Donut** - Rp 25,000
4. **Matcha Cake** - Rp 55,000

### Customers (Can place orders)
1. **John Doe** - john@example.com
2. **Jane Smith** - jane@example.com

## 📚 Documentation

For detailed information:
- Full documentation: See `README.md`
- API endpoints: See `documentation/Pastry_API.postman_collection.json`
- Database schema: See `README.md` → "Database Schema" section

## ⚙️ Configuration

Edit `.env` file to change:
- Ports: API_GATEWAY_PORT, *_SERVICE_PORT
- MySQL credentials: MYSQL_USER, MYSQL_PASSWORD
- JWT secret: JWT_SECRET_KEY

## ✨ Tips

1. **Keep browser DevTools open** (F12) to see any errors
2. **Check terminal output** for backend errors
3. **Clear localStorage** if having login issues: 
   ```javascript
   localStorage.clear()
   ```
4. **Use Postman** for API testing (import `Pastry_API.postman_collection.json`)

## 🎯 Next Steps

1. Test with sample data
2. Explore Admin dashboard
3. Try updating order status
4. Test with Postman collection
5. Modify menu items and add custom items
6. Experiment with different order flows

## 📞 Need Help?

Check the main `README.md` file for:
- Complete API documentation
- Database schema details
- Architecture explanation
- Security notes
- Performance optimization tips

---

**You're all set! Start exploring the Pastry Delivery System! 🥐**
