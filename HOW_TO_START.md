# 🚀 How to Start PastryApp - Manual Steps

## Option 1: Quick Start (Recommended)

```bash
# Navigate to project root
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp

# Make startup script executable and run it
chmod +x STARTUP.sh
./STARTUP.sh
```

This will automatically start all services and open everything you need!

---

## Option 2: Manual Startup (6 Terminal Windows)

### Prerequisites
- MySQL must be running
- All Python dependencies installed (already done ✅)

### Step 1: Kill any old processes (Terminal 1)

```bash
killall Python 2>/dev/null || true
sleep 1
```

### Step 2: Initialize Database (Terminal 1)

```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/backend
source venv/bin/activate
python3 init_db.py
```

Expected output:
```
🔧 Creating database and tables...
✅ All tables created successfully!
✅ Sample data inserted successfully!
```

---

### Terminal 1: API Gateway (Port 5050)

```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/backend
source venv/bin/activate
cd api_gateway
python3 app.py
```

Expected:
```
 * Running on http://127.0.0.1:5050
```

---

### Terminal 2: Customer Service (Port 5001)

```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/backend
source venv/bin/activate
cd services/customer_service
python3 app.py
```

Expected:
```
 * Running on http://127.0.0.1:5001
```

---

### Terminal 3: Menu Service (Port 5003)

```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/backend
source venv/bin/activate
cd services/menu_service
python3 app.py
```

Expected:
```
 * Running on http://127.0.0.1:5003
```

---

### Terminal 4: Order Service (Port 5004)

```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/backend
source venv/bin/activate
cd services/order_service
python3 app.py
```

Expected:
```
 * Running on http://127.0.0.1:5004
```

---

### Terminal 5: Frontend Server (Port 8000)

```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/frontend
python3 -m http.server 8000
```

Expected:
```
Serving HTTP on :: port 8000
```

---

## Step 3: Access the Application

Open your browser and visit:

- **Customer Interface**: http://localhost:8000/index.html
- **Admin Dashboard**: http://localhost:8000/admin.html

---

## 🔐 Test Credentials

| Role | Username | Password |
|------|----------|----------|
| Customer | `customer` | `iamcustomer` |
| Admin | `admin` | `iamadmin` |

---

## 📊 Verify Services Are Running

In a new terminal, run:

```bash
netstat -an | grep -E '5050|5001|5003|5004|8000' | grep LISTEN
```

You should see 5 lines showing ports 5050, 5001, 5003, 5004, and 8000 all LISTEN.

---

## 🛑 Stopping Services

### Option 1: Kill all Python processes
```bash
killall Python
```

### Option 2: Individual terminal windows
- Press `Ctrl+C` in each terminal window

---

## 🐛 Troubleshooting

### Port Already In Use
```bash
# Find what's using port 5050
lsof -i :5050

# Kill the process
kill -9 <PID>
```

### ModuleNotFoundError
Make sure you activated the virtual environment:
```bash
cd /Users/luckygirlsyndrome/Documents/College/IAE-PROJECTS/PastryApp/backend
source venv/bin/activate
```

### MySQL Connection Error
Make sure MySQL is running:
```bash
# On macOS
brew services start mysql

# Check status
brew services list | grep mysql
```

### Python Command Not Found
Use `python3` instead of `python`:
```bash
# ❌ Wrong
python app.py

# ✅ Correct
python3 app.py
```

---

## 📁 Project Structure

```
PastryApp/
├── backend/
│   ├── venv/                          # Virtual environment
│   ├── .env                           # Configuration (port 5050 for gateway)
│   ├── init_db.py                     # Database initialization
│   ├── requirements.txt               # Dependencies
│   ├── api_gateway/
│   │   └── app.py                     # API Gateway (Port 5050)
│   └── services/
│       ├── customer_service/app.py    # Port 5001
│       ├── menu_service/app.py        # Port 5003
│       └── order_service/app.py       # Port 5004
├── frontend/
│   ├── index.html                     # Customer Interface
│   └── admin.html                     # Admin Dashboard
└── STARTUP.sh                         # One-click startup script
```

---

## 🎯 Quick Reference

**Start Everything**: `./STARTUP.sh`

**Manual Start (5 terminals needed)**:
1. Terminal 1: `cd backend && source venv/bin/activate && cd api_gateway && python3 app.py`
2. Terminal 2: `cd backend && source venv/bin/activate && cd services/customer_service && python3 app.py`
3. Terminal 3: `cd backend && source venv/bin/activate && cd services/menu_service && python3 app.py`
4. Terminal 4: `cd backend && source venv/bin/activate && cd services/order_service && python3 app.py`
5. Terminal 5: `cd frontend && python3 -m http.server 8000`

**Access**: 
- Customer: http://localhost:8000/index.html
- Admin: http://localhost:8000/admin.html

---

## ✅ What Each Service Does

| Service | Port | Purpose |
|---------|------|---------|
| API Gateway | 5050 | JWT authentication, routing to services |
| Customer Service | 5001 | Customer CRUD operations |
| Menu Service | 5003 | Menu items management |
| Order Service | 5004 | Order management & tracking |
| Frontend | 8000 | Web interface |

---

Good luck! 🍰🚀
