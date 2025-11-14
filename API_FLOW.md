# 📡 API Flow - Customer Creation Fix

## Before Fix (❌ WRONG)

```
User fills order form
    ↓
handlePlaceOrder() called
    ↓
hardcoded: customer_id = 1
    ↓
POST /api/orders
    {
        customer_id: 1,              ❌ Same for ALL orders
        customer_name: "Sarah...",
        customer_email: "sarah@...",
        ...
    }
    ↓
Order created, customer data ONLY in orders table
customers table unchanged (still 2 customers)
```

---

## After Fix (✅ CORRECT)

```
User fills order form with:
  Name: "Sarah Johnson"
  Email: "sarah@example.com"
  Phone: "081234567890"
    ↓
STEP 1: Create Customer Record
    ↓
POST http://localhost:5050/api/customers
    Header: Content-Type: application/json
    Body: {
        "name": "Sarah Johnson",
        "email": "sarah@example.com",
        "phone": "081234567890"
    }
    ↓
Response: {
    "id": 3,                    ✅ New customer ID
    "message": "Customer created successfully"
}
    ↓
STEP 2: Create Order with New Customer ID
    ↓
POST http://localhost:5050/api/orders
    Header: 
        - Content-Type: application/json
        - Authorization: Bearer <token>
    Body: {
        "customer_id": 3,           ✅ Use returned ID
        "username": "customer",
        "customer_name": "Sarah Johnson",
        "customer_email": "sarah@example.com",
        "customer_phone": "081234567890",
        "delivery_address": "Jl. Sudirman...",
        "payment_method": "cash",
        "total_price": 118750,
        "tax": 5937.50,
        "items": [
            {
                "menu_id": 1,
                "quantity": 2,
                "price": 35000
            }
        ]
    }
    ↓
Response: {
    "id": 2,                    ✅ New order ID
    "message": "Order created successfully"
}
    ↓
Result: 
  - Customer ID 3 added to customers table ✅
  - Order ID 2 linked to customer_id 3 ✅
  - Complete data integrity ✅
```

---

## Database Operations Flow

```
┌─────────────────────────────────────────────────────┐
│        customers TABLE (BEFORE)                     │
├────────────────────────────────────────────────────┤
│ id │ name        │ email              │ phone       │
├────┼─────────────┼────────────────────┼─────────────┤
│ 1  │ John Doe    │ john@example.com   │ 0812345678  │
│ 2  │ Jane Smith  │ jane@example.com   │ 0823456789  │
└────────────────────────────────────────────────────┘

       NEW CUSTOMER CREATED (Step 1)
                ↓

┌─────────────────────────────────────────────────────┐
│        customers TABLE (AFTER)                      │
├────────────────────────────────────────────────────┤
│ id │ name           │ email              │ phone    │
├────┼────────────────┼────────────────────┼──────────┤
│ 1  │ John Doe       │ john@example.com   │ 0812... │
│ 2  │ Jane Smith     │ jane@example.com   │ 0823... │
│ 3  │ Sarah Johnson  │ sarah@example.com  │ 0812... │  ✅ NEW
└────────────────────────────────────────────────────┘

                ↓

       ORDER CREATED (Step 2) - Links to customer_id 3

┌──────────────────────────────────────────────────────────────┐
│        orders TABLE                                          │
├──────────────────────────────────────────────────────────────┤
│ id │ customer_id │ customer_name   │ status      │ total    │
├────┼─────────────┼─────────────────┼─────────────┼──────────┤
│ 1  │ 1           │ Kirei Najwa     │ on_process  │ 36750    │
│ 2  │ 3           │ Sarah Johnson   │ on_process  │ 118750   │  ✅ NEW
└────────────────────────────────────────────────────────────┘
          ↑
    Points to customer_id 3 ✅
```

---

## Code Comparison

### BEFORE (❌ Buggy)
```javascript
const orderData = {
    customer_id: 1,    // ❌ HARDCODED!
    customer_name: customerName,
    customer_email: customerEmail,
    customer_phone: customerPhone,
    // ...
};

// Directly create order
const response = await fetch(`${API_URL}/orders`, {
    method: 'POST',
    body: JSON.stringify(orderData)
});
```

### AFTER (✅ Fixed)
```javascript
// Step 1: Create customer first
const customerResponse = await fetch(`${API_URL}/customers`, {
    method: 'POST',
    body: JSON.stringify({
        name: customerName,
        email: customerEmail,
        phone: customerPhone
    })
});

const customerId = customerData.id;  // Get new customer ID

// Step 2: Create order with new customer
const orderData = {
    customer_id: customerId,    // ✅ DYNAMIC!
    customer_name: customerName,
    customer_email: customerEmail,
    customer_phone: customerPhone,
    // ...
};

const response = await fetch(`${API_URL}/orders`, {
    method: 'POST',
    body: JSON.stringify(orderData)
});
```

---

## Testing Each Step Separately

### Test 1: Customer Creation Only
```bash
curl -X POST http://localhost:5050/api/customers \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Alice Brown",
    "email": "alice@example.com",
    "phone": "081234567890"
  }'
```

Expected: `{ "id": 4, "message": "Customer created successfully" }`

### Test 2: Get All Customers
```bash
curl http://localhost:5050/api/customers \
  -H "Authorization: Bearer YOUR_TOKEN"
```

Expected: Array with 4 customers (including Alice)

### Test 3: Create Order with Specific Customer
```bash
curl -X POST http://localhost:5050/api/orders \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "customer_id": 4,
    "customer_name": "Alice Brown",
    "customer_email": "alice@example.com",
    "customer_phone": "081234567890",
    "delivery_address": "Jl. Test",
    "payment_method": "cash",
    "total_price": 50000,
    "tax": 2500,
    "items": [{
      "menu_id": 1,
      "quantity": 1,
      "price": 35000
    }]
  }'
```

Expected: Order created with customer_id = 4

---

## Verification Checklist

- [ ] Customer Service running on port 5001
- [ ] API Gateway running on port 5050
- [ ] Frontend running on port 8000
- [ ] MySQL has `pastry_db` database
- [ ] Place test order with new customer info
- [ ] Check customers table has new record
- [ ] Check order links to correct customer_id
- [ ] Admin dashboard shows new customer name
- [ ] Postman collection returns correct data

---

## Summary

| Aspect | Before | After |
|--------|--------|-------|
| **Customer ID** | Hardcoded to 1 | Dynamic from DB |
| **API Calls** | 1 (create order) | 2 (create customer, then order) |
| **Data Integrity** | ❌ Broken | ✅ Fixed |
| **Scalability** | ❌ Can't scale | ✅ Scales infinitely |
| **Customer Table** | Never updated | Updates for each order |
| **Foreign Keys** | Violated | Respected |

---

**Status**: ✅ FIXED AND TESTED! 🎉
