# 🎯 Running Multiple Roles Simultaneously

## Quick Answer

Use **different browser windows or tabs** with **private/incognito mode** to run customer and admin at the same time!

---

## 🚀 Method 1: Different Browser Windows (Easiest)

### Step 1: Start Services
```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp
./STARTUP.sh
```

### Step 2: Open Window 1 - Customer
1. Open **Regular Browser Window** #1
2. Go to: `http://localhost:8000/index.html`
3. Click "Login"
4. Enter:
   - Username: `customer`
   - Password: `iamcustomer`
   - Role: **Customer**
5. Click Login
6. **You're now logged in as CUSTOMER** ✅

### Step 3: Open Window 2 - Admin
1. Open **NEW Regular Browser Window** #2
2. Go to: `http://localhost:8000/admin.html`
3. You'll be redirected to login page
4. Click "Login"
5. Enter:
   - Username: `admin`
   - Password: `iamadmin`
   - Role: **Admin**
6. Click Login
7. **You're now logged in as ADMIN** ✅

### Result
- **Window 1**: Customer browsing menu, placing orders
- **Window 2**: Admin managing orders in real-time
- Both connected to same backend ✅

---

## 🔄 Method 2: Different Tabs with Incognito Mode

### Why Incognito?
- Separate localStorage for each incognito window
- Different cookies/sessions
- True separation between logins

### Step 1: Open Regular Tab (Customer)
1. Open normal tab: `http://localhost:8000/index.html`
2. Login as **customer**

### Step 2: Open Incognito Tab (Admin)
1. Press: `Cmd + Shift + N` (macOS) or `Ctrl + Shift + N` (Windows/Linux)
2. Go to: `http://localhost:8000/admin.html`
3. Login as **admin**

### Result
- **Regular tab**: Customer view
- **Incognito tab**: Admin view (separate localStorage)
- Can test interactions between roles

---

## 🎬 Testing Workflow - Both Roles Active

### Phase 1: Customer Places Order (Window 1)
```
1. In Customer window:
   - Browse menu
   - Add 2-3 items to cart
   - Fill delivery form with:
     Name: Test Customer
     Email: test@example.com
     Phone: 081234567890
     Address: Jl. Test St
   - Click "Place Order"
   - See receipt with Order ID (e.g., #5)
```

### Phase 2: Admin Sees Order Update (Window 2)
```
2. In Admin window:
   - Should auto-refresh every 10 seconds
   - Look for Order #5 in the table
   - See: Test Customer, Status: On Process
   - NEW order appears in real-time ✅
```

### Phase 3: Admin Updates Status (Window 2)
```
3. In Admin window:
   - Click status badge for Order #5
   - Select "On Delivery"
   - Order status updates
```

### Phase 4: Customer Sees Update (Window 1)
```
4. In Customer window:
   - Scroll to "Your Orders"
   - Order #5 now shows: "On Delivery" ✅
   - Status updated in real-time
```

---

## 🔍 Multi-Role Test Scenarios

### Scenario 1: Customer Orders, Admin Manages
```
Time    | Window 1 (Customer)      | Window 2 (Admin)
--------|--------------------------|---------------------------
0:00    | Browse menu              | View dashboard (0 orders)
0:30    | Add items to cart        | (Idle)
1:00    | Place order #1           | (Idle)
1:05    | See receipt              | Auto-refresh: Order #1 appears ✅
1:10    | (Idle)                   | Click status: On Delivery
1:15    | See order updated ✅     | Dashboard shows updated
2:00    | Place order #2           | (Idle)
2:05    | See receipt              | Auto-refresh: Order #2 appears ✅
```

### Scenario 2: Stress Test - Multiple Orders
```
1. Customer window: Place 3 orders rapidly
2. Admin window: Watch all 3 appear in real-time
3. Admin updates statuses on all 3
4. Customer sees all status changes
```

### Scenario 3: Check Database Integrity
```
1. Customer places order
2. Admin updates status
3. Open Postman or MySQL client
4. Verify data in database:
   - customers table has new customer
   - orders table has new order
   - order status matches what admin set
```

---

## 📊 Testing Matrix

| Feature | Customer | Admin | Test |
|---------|----------|-------|------|
| Browse menu | ✅ | ❌ | Window 1 only |
| Place order | ✅ | ❌ | Window 1 |
| See my orders | ✅ | N/A | Window 1 |
| View all orders | ❌ | ✅ | Window 2 |
| Update status | ❌ | ✅ | Window 2 |
| Real-time sync | ✅ | ✅ | Both windows |

---

## 🎮 Interactive Test Guide

### 5-Minute Test

**Step 1: Setup (1 min)**
- Start services: `./STARTUP.sh`
- Open Window 1 & 2

**Step 2: Customer Actions (2 min)**
- Window 1: Login as customer
- Add items to cart
- Place order

**Step 3: Admin Actions (2 min)**
- Window 2: Login as admin
- Find your order
- Update status
- See customer notification

---

## 🔐 Login Credentials Reminder

### Customer Account
```
Username: customer
Password: iamcustomer
Role: Customer
```

### Admin Account
```
Username: admin
Password: iamadmin
Role: Admin
```

---

## 💾 LocalStorage Separation

Each window has its own localStorage:

**Window 1 (Customer)**
```javascript
localStorage.getItem('authToken')    // Customer token
localStorage.getItem('currentUser')  // {role: 'customer'}
localStorage.getItem('cart')         // Cart items
```

**Window 2 (Admin)**
```javascript
localStorage.getItem('authToken')    // Admin token
localStorage.getItem('currentUser')  // {role: 'admin'}
localStorage.getItem('cart')         // Empty (admin doesn't use)
```

If same window/tab, second login overwrites first!

---

## 🐛 Troubleshooting

### Issue: Still logged in as customer in Window 2
**Solution**: 
- Clear browser cache/cookies for admin window
- Use incognito/private mode for one of them
- Or logout in Window 1 first

### Issue: Admin doesn't see customer's new order
**Solution**:
- Check auto-refresh is working (every 10 seconds)
- Click "Refresh" button manually
- Make sure both windows use port 8000 (not different ports)

### Issue: Status update doesn't show in customer window
**Solution**:
- Refresh Window 1 manually
- Wait for auto-refresh (10 seconds)
- Check console for errors (F12)

### Issue: Different data in two windows
**Solution**:
- Make sure services are running on same ports
- Both using `http://localhost:8000/`
- Not using different instances of backend

---

## 🎯 Real-World Use Cases

### Use Case 1: Demonstration
```
Show customer browsing → admin managing
Perfect for presentations/demos
```

### Use Case 2: Testing
```
Place orders as customer
Update status as admin
Verify customer sees updates
Test all workflows
```

### Use Case 3: Development
```
Debug customer-side issues in Window 1
Debug admin-side issues in Window 2
Test API integration in both roles
```

### Use Case 4: Training
```
Show trainees how system works
Window 1: Customer perspective
Window 2: Admin perspective
```

---

## 🔄 Advanced: Three Roles (if you add more)

```
Window 1: Customer (regular)
Window 2: Admin (incognito)
Window 3: Restaurant (future) (private window)
```

Each window: separate browser context = separate localStorage

---

## ✨ Best Setup for Testing

```
┌─────────────────────────────────────────────┐
│           Your Computer                     │
├─────────────────────────────────────────────┤
│                                             │
│  Terminal (running services on ports)       │
│  ├─ Port 5050: API Gateway ✅              │
│  ├─ Port 5001: Customer Service ✅        │
│  ├─ Port 5003: Menu Service ✅            │
│  ├─ Port 5004: Order Service ✅           │
│  └─ Port 8000: Frontend Server ✅         │
│                                             │
│  Browser Window 1          Browser Window 2 │
│  ├─ http://localhost:8000  ├─ http://localhost:8000
│  │  index.html             │  admin.html    │
│  │  Role: Customer         │  Role: Admin   │
│  │                         │                │
│  │ ✅ Menu               │ ✅ Orders      │
│  │ ✅ Cart               │ ✅ Status Mgmt │
│  │ ✅ My Orders          │ ✅ Real-time   │
│  └─ (Auto-refresh)        └─ (Auto-refresh)
│                                             │
│  Both windows ←→ Same Backend ✅           │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 🚀 Quick Start Commands

```bash
# Terminal 1: Start all services
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp
./STARTUP.sh

# Terminal 2: (Optional) Watch logs
tail -f /tmp/api_gateway.log

# Browser Window 1
open http://localhost:8000/index.html    # Login as customer

# Browser Window 2
open http://localhost:8000/admin.html    # Login as admin
```

---

## 📈 Performance Tips

1. **Don't open too many windows** - Each uses RAM/CPU
2. **Use same browser** - Chrome, Firefox, Safari all work
3. **Keep services running** - Don't stop backend while testing
4. **Check console** - F12 to see any errors
5. **Auto-refresh** - Both windows refresh every 10 seconds

---

## ✅ Verification Checklist

- [ ] Both windows show correct role in header
- [ ] Customer can place order
- [ ] Admin sees order within 10 seconds
- [ ] Admin can update status
- [ ] Customer sees status update within 10 seconds
- [ ] No errors in browser console (F12)
- [ ] Backend logs show API calls
- [ ] Data persists in database

---

**Status**: ✅ **READY TO TEST MULTI-ROLE!** 🎉

Now you can run customer and admin simultaneously and test real-time interactions!
