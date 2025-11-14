# ⚡ Quick Start Card

## 🚀 Start Everything (ONE Command)

```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp
chmod +x STARTUP.sh
./STARTUP.sh
```

This automatically starts:
- ✅ API Gateway (Port 5050)
- ✅ Customer Service (Port 5001)
- ✅ Menu Service (Port 5003)
- ✅ Order Service (Port 5004)
- ✅ Frontend Server (Port 8000)

---

## 🌐 Access URLs

| What | URL |
|------|-----|
| **Customer Interface** | http://localhost:8000/index.html |
| **Admin Dashboard** | http://localhost:8000/admin.html |
| **API Base** | http://localhost:5050/api |
| **API Login** | http://localhost:5050/api/login |

---

## 🔐 Login Credentials

```
Customer:
  Username: customer
  Password: iamcustomer

Admin:
  Username: admin
  Password: iamadmin
```

---

## 📍 Port Mapping

```
Port 5050 → API Gateway (Main entry point) ⭐
Port 5001 → Customer Service (internal)
Port 5003 → Menu Service (internal)
Port 5004 → Order Service (internal)
Port 8000 → Frontend Server (Web UI)
```

**Why 5050?** Port 5000 is used by macOS AirPlay.

---

## 🛑 Stop Services

```bash
killall Python
```

Or press `Ctrl+C` in each terminal.

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| `HOW_TO_START.md` | Detailed manual startup steps |
| `PORT_CONFIG.md` | Port explanation & API reference |
| `STARTUP.sh` | Automated startup script |
| `README.md` | Full project documentation |
| `ARCHITECTURE.md` | System design & flows |

---

## 🧪 Test the API

### Using Postman
1. Import: `/documentation/Pastry_API.postman_collection.json`
2. baseUrl is already set to `http://localhost:5050/api`
3. Login first to get token
4. Test any endpoint

### Using cURL
```bash
# Login
curl -X POST http://localhost:5050/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"customer","password":"iamcustomer","role":"customer"}'

# Get all menus (no auth needed)
curl http://localhost:5050/api/menus

# Get orders (needs token from login)
curl -H "Authorization: Bearer YOUR_TOKEN" \
  http://localhost:5050/api/orders
```

---

## ✨ Key Features

✅ Dual-role login (Customer & Admin)
✅ Real-time order tracking
✅ Beautiful animations
✅ Responsive design
✅ JWT authentication
✅ Role-based access control
✅ MySQL database
✅ Microservices architecture

---

## 📁 Project Structure

```
PastryApp/
├── backend/
│   ├── api_gateway/app.py          ← Port 5050
│   ├── services/
│   │   ├── customer_service/       ← Port 5001
│   │   ├── menu_service/           ← Port 5003
│   │   └── order_service/          ← Port 5004
│   ├── venv/                       ← Virtual environment
│   ├── init_db.py                  ← Database setup
│   └── .env                        ← Configuration
├── frontend/
│   ├── index.html                  ← Customer UI
│   └── admin.html                  ← Admin UI
├── documentation/
│   └── Postman_API.postman_collection.json
└── HOW_TO_START.md                 ← This file
```

---

## 🐛 Troubleshooting

**"Port already in use"**
```bash
lsof -i :5050      # See what's using it
kill -9 <PID>      # Kill the process
```

**"Command not found: python"**
Use `python3` instead of `python`

**"ModuleNotFoundError"**
Make sure venv is activated:
```bash
source backend/venv/bin/activate
```

**"Can't connect to API"**
Check if services are running:
```bash
netstat -an | grep -E '5050|5001|5003|5004|8000' | grep LISTEN
```

Should show 5 LISTEN entries.

---

## 🎯 Next Steps

1. ✅ **Start services**: `./STARTUP.sh`
2. 🌐 **Open browser**: http://localhost:8000/index.html
3. 🔐 **Login** with customer credentials
4. 🛒 **Browse menu** and place an order
5. 👁️ **View orders** with live status updates
6. 📊 **Check admin dashboard** at http://localhost:8000/admin.html

---

**Questions?** Check `HOW_TO_START.md` for detailed instructions! 🚀
