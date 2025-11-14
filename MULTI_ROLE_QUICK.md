# 🎬 Multi-Role Testing - Quick Reference

## 30-Second Setup

```bash
# 1. Start everything
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp
./STARTUP.sh

# 2. Open Window 1 (Customer)
# URL: http://localhost:8000/index.html
# Login: customer / iamcustomer / Role: Customer

# 3. Open Window 2 (Admin)  
# URL: http://localhost:8000/admin.html
# Login: admin / iamadmin / Role: Admin

# 4. Done! 🎉
```

---

## Side-by-Side Comparison

```
┌────────────────────┬────────────────────┐
│   Window 1         │   Window 2         │
│   CUSTOMER         │   ADMIN            │
├────────────────────┼────────────────────┤
│                    │                    │
│ [🥐 Menu Items]    │ [📊 Dashboard]     │
│ • Add to Cart      │ • Orders Table     │
│ • Place Order      │ • Status Dropdown  │
│ • Track Orders     │ • Real-time Stats  │
│                    │                    │
│ Credentials:       │ Credentials:       │
│ customer           │ admin              │
│ iamcustomer        │ iamadmin           │
│                    │                    │
│ ↔ Synced Backend   │ ↔ Synced Backend   │
│                    │                    │
└────────────────────┴────────────────────┘
```

---

## 5-Minute Full Test

### Minute 1: Setup
```
Start services
Terminal: ./STARTUP.sh
Wait for "All services started"
```

### Minute 2: Customer Login
```
Window 1: http://localhost:8000/index.html
Click Login
Enter: customer / iamcustomer / Customer
Should see menu 📋
```

### Minute 3: Admin Login
```
Window 2: http://localhost:8000/admin.html
Redirects to login
Enter: admin / iamadmin / Admin
Should see dashboard 📊
```

### Minute 4: Customer Orders
```
Window 1:
Add 2 items to cart
Fill delivery form
Click "Place Order"
See receipt ✅
```

### Minute 5: Admin Sees + Updates
```
Window 2:
Look at orders table
Find your order
Click status: On Delivery
Window 1 refreshes and shows update ✅
```

---

## What You Can Test

| Action | Window | See In | Time |
|--------|--------|--------|------|
| Add menu item | 1 | 1 | Instant |
| Place order | 1 | 2 | 10 sec |
| Update status | 2 | 1 | 10 sec |
| Delete order | 2 | 1 | 10 sec |
| View details | 2 | 2 | Instant |

---

## Browser Setup Options

### Option A: Two Regular Windows
```
Window 1: Regular Chrome
Window 2: Regular Firefox
OR
Window 1: Regular Chrome
Window 2: Chrome Private Window
```
✅ Easiest | Works great

### Option B: Incognito Mode
```
Tab 1: Regular Mode → Customer
Tab 2: Incognito Mode → Admin
```
✅ Single browser | Separate sessions

### Option C: Multiple Browsers
```
Chrome → Customer
Firefox → Admin
Safari → Testing
```
✅ Most isolation | Most resources

---

## Real-Time Interaction Flow

```
TIME    WINDOW 1 (Customer)      WINDOW 2 (Admin)
────────────────────────────────────────────
0:00    Browsing menu            Viewing dashboard (0 orders)
1:00    Adds 2 items to cart     [Idle]
2:00    Fills delivery form      [Idle]
3:00    ⬇️ Places Order #5 ⬇️    [Waiting...]
3:05    ✅ Receipt shows         [Auto-refresh triggers]
3:10    [Idle]                   ✅ Order #5 appears in table!
4:00    [Idle]                   ⬆️ Clicks Status: On Delivery ⬆️
4:05    [Waiting...]             ✅ Status updated
4:10    ✅ "Your Orders"         [Idle]
        shows "On Delivery"      
```

---

## Common Issues & Quick Fixes

| Problem | Fix |
|---------|-----|
| Window 2 logs out Window 1 | Use incognito for one |
| Admin sees no orders | Click Refresh or wait 10 sec |
| Status update doesn't show | Refresh Window 1 manually |
| Can't login as admin | Make sure you select "Admin" role |
| 404 error | Services not running - check STARTUP.sh |

---

## Verification Checklist

```
✅ Window 1 shows customer menu
✅ Window 2 shows admin dashboard
✅ Customer can place order
✅ Admin sees order within 10 sec
✅ Admin can update status
✅ Customer sees status change
✅ No errors in console (F12)
✅ Database updated (check MySQL)
```

---

## URLs Reference

| Role | URL |
|------|-----|
| Customer | http://localhost:8000/index.html |
| Admin | http://localhost:8000/admin.html |
| API | http://localhost:5050/api |
| Postman | Import from documentation/ |

---

## Credentials Reference

| Role | Username | Password |
|------|----------|----------|
| Customer | customer | iamcustomer |
| Admin | admin | iamadmin |

---

## Port Reference

| Service | Port |
|---------|------|
| API Gateway | 5050 |
| Customer Service | 5001 |
| Menu Service | 5003 |
| Order Service | 5004 |
| Frontend | 8000 |

---

## 🎯 Now Go Test!

1. Open MULTI_ROLE_TESTING.md for detailed guide
2. Start services: `./STARTUP.sh`
3. Open 2 windows
4. Login with different roles
5. Test interactions
6. Verify database

---

**Ready?** Go to the full guide: `MULTI_ROLE_TESTING.md` 🚀
