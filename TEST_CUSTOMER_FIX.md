# 🔧 Testing the Customer Fix

## ✅ What's Fixed

Now when you:
1. **Place an order** with new customer details
2. A **new customer record** is created in the `customers` table
3. The **order is linked** to that customer via `customer_id`
4. You can see the customer in both:
   - The **customers API endpoint** (`/api/customers`)
   - The **orders table** (with proper foreign key relationship)

---

## 🧪 Complete Test Workflow

### Step 1: Start Everything
```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp
./STARTUP.sh
```

Wait for all services to start (should see 5 LISTEN ports).

---

### Step 2: Open Postman & Get Initial Data

**Check Customers Before Order:**
```
GET http://localhost:5050/api/customers
Authorization: Bearer {{token}}
```

Expected: Only 2 customers (John Doe, Jane Smith)

**Check Orders Before:**
```
GET http://localhost:5050/api/orders
Authorization: Bearer {{token}}
```

Expected: 1 order (from sample data)

---

### Step 3: Place Order with New Customer (Using Frontend)

1. Open browser: `http://localhost:8000/index.html`
2. Click **Login**
3. Enter: `customer / iamcustomer`
4. Add items to cart (click "Add to Cart" on 2-3 pastries)
5. Scroll to "Delivery Details"
6. **Enter NEW customer information:**
   - Name: `Sarah Johnson`
   - Email: `sarah@example.com`
   - Phone: `081234567890`
   - Address: `Jl. Sudirman No. 456, Jakarta`
   - Payment: Cash on Delivery
7. Click **Place Order**
8. You should see a receipt with new Order ID

---

### Step 4: Verify Customer Was Created (Postman)

**Check Customers Again:**
```
GET http://localhost:5050/api/customers
Authorization: Bearer {{token}}
```

Expected response:
```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "081234567890",
    "created_at": "2025-11-13T..."
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "jane@example.com",
    "phone": "082345678901",
    "created_at": "2025-11-13T..."
  },
  {
    "id": 3,
    "name": "Sarah Johnson",        // ✅ NEW!
    "email": "sarah@example.com",   // ✅ NEW!
    "phone": "081234567890",        // ✅ NEW!
    "created_at": "2025-11-13T..."
  }
]
```

---

### Step 5: Verify Order Links to Correct Customer

**Get New Order:**
```
GET http://localhost:5050/api/orders/2
Authorization: Bearer {{token}}
```

Expected response shows:
```json
{
  "id": 2,
  "customer_id": 3,              
  "customer_name": "Sarah Johnson",
  "customer_email": "sarah@example.com",
  "customer_phone": "081234567890",
  "delivery_address": "Jl. Sudirman No. 456, Jakarta",
  "status": "on_process",
  "items": [
    {
      "menu_id": 1,
      "quantity": 2,
      "price": "35000.00"
    },
    {
      "menu_id": 2,
      "quantity": 1,
      "price": "45000.00"
    }
  ],
  "total_price": "118750.00",
  "tax": "5937.50"
}
```

---

### Step 6: Test Admin Dashboard

1. Go to: `http://localhost:8000/admin.html`
2. Login with: `admin / iamadmin`
3. Look at the Orders table
4. You should see your new order with:
   - Order ID (e.g., #2)
   - Customer: Sarah Johnson ✅
   - Status: On Process
   - Total: Rp 118,750

---

## 📊 Compare: Before vs After

### BEFORE FIX ❌
```
Frontend places order with "Sarah Johnson"
            ↓
Order created with hardcoded customer_id = 1
            ↓
Result: Order linked to "John Doe" (wrong customer!)
            ↓
customers table: Still only 2 customers
orders table: Shows Sarah Johnson but customer_id = 1 (inconsistent)
```

### AFTER FIX ✅
```
Frontend places order with "Sarah Johnson"
            ↓
Step 1: Create new customer in customers table
            ↓
Get new customer_id = 3
            ↓
Step 2: Create order with customer_id = 3
            ↓
Result: Order properly linked to "Sarah Johnson"
            ↓
customers table: Now has 3 customers (John, Jane, Sarah)
orders table: Shows Sarah Johnson with customer_id = 3 (consistent!)
```

---

## 🎯 Key Validations

✅ **Database Integrity**: Customer exists in `customers` table
✅ **Foreign Key Relationship**: Order's `customer_id` matches a real customer
✅ **Data Consistency**: Order customer name matches the customer record
✅ **Scalability**: Each new order creates its own customer (not hardcoded to ID 1)
✅ **Admin Dashboard**: Shows correct customer name for each order

---

## 🐛 If You See Issues

**Issue: Customer still not showing in customers table**
- Check the Postman response to customer creation endpoint
- Make sure services are running: `netstat -an | grep LISTEN | grep -E '5050|5001'`
- Check backend logs for errors

**Issue: Order shows wrong customer_id**
- Restart the frontend page (clear cache)
- Make sure you're logged in before placing order
- Check authorization headers are being sent

**Issue: "Failed to create customer record" error**
- Make sure Customer Service is running on port 5001
- Check MySQL is running
- Try creating customer directly in Postman first

---

## 🚀 Next Improvements

1. **Prevent Duplicate Customers**
   - Check if email already exists before creating
   - Reuse existing customer if email matches

2. **Auto-Login New Customers**
   - After creating customer, auto-login with that account
   - Store customer profile in localStorage

3. **Customer Portal**
   - View all past orders
   - Update delivery address
   - Track real-time delivery

---

**Test this now!** 🧪 Place an order and verify the customer shows up in the database! 🎉
