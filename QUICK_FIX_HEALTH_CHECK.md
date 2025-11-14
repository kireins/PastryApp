# 🔧 Quick Fix: Health Check Connection Refused

## ❌ Masalah
Error `ERR_CONNECTION_REFUSED` ketika mengakses `http://localhost:5000/api/health`

## ✅ Solusi: Start API Gateway Service

### Cara 1: Menggunakan Batch Script (Recommended)

1. **Jalankan script startup:**
   ```bash
   start-all-services.bat
   ```
   
2. Script akan otomatis:
   - Initialize database
   - Start API Gateway di port 5000
   - Start semua microservices
   - Start frontend

3. **Tunggu beberapa detik** sampai semua service running

4. **Cek di browser:**
   - http://localhost:5000/api/health

---

### Cara 2: Manual Start (Jika script tidak bekerja)

**Terminal 1 - API Gateway:**
```bash
cd backend/api_gateway
..\venv\Scripts\activate.bat
python app.py
```

**Terminal 2 - Customer Service:**
```bash
cd backend/services/customer_service
..\..\venv\Scripts\activate.bat
python app.py
```

**Terminal 3 - Menu Service:**
```bash
cd backend/services/menu_service
..\..\venv\Scripts\activate.bat
python app.py
```

**Terminal 4 - Order Service:**
```bash
cd backend/services/order_service
..\..\venv\Scripts\activate.bat
python app.py
```

---

## ✅ Verifikasi Service Running

Setelah start, cek di browser:

1. **API Gateway**: http://localhost:5000/api/health
   - Harus return: `{"status": "API Gateway is running"}`

2. **Customer Service**: http://localhost:5001/health
   - Harus return: `{"status": "Customer Service is running"}`

3. **Menu Service**: http://localhost:5003/health
   - Harus return: `{"status": "Menu Service is running"}`

4. **Order Service**: http://localhost:5004/health
   - Harus return: `{"status": "Order Service is running"}`

---

## ⚠️ Troubleshooting

### Port sudah digunakan?
```bash
# Cek port yang digunakan
netstat -ano | findstr :5000
netstat -ano | findstr :5001
netstat -ano | findstr :5003
netstat -ano | findstr :5004
```

### Service tidak start?
1. Cek apakah virtual environment sudah diaktifkan
2. Cek apakah `.env` file ada di `backend/.env`
3. Cek apakah MySQL service running
4. Lihat error message di terminal window

### Database connection error?
- Pastikan MySQL service running
- Cek konfigurasi di `backend/.env`
- Pastikan database `pastry_db` sudah dibuat (jalankan `python backend/init_db.py`)

---

## 📝 Catatan

- **Port API Gateway**: 5000 (bukan 5050)
- **Health check endpoint**: `/api/health` (dengan prefix `/api`)
- **Service health check**: `/health` (tanpa prefix)

