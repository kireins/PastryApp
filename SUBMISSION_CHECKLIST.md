# ✅ Submission Checklist

Checklist final sebelum submit proyek Pastry Delivery System.

---

## 📁 1. Code + README.md (Root)

- [ ] **README.md** ada di root folder
- [ ] README.md berisi:
  - [ ] Deskripsi singkat proyek & topik
  - [ ] Arsitektur: Client → API Gateway → Services → DB
  - [ ] Cara menjalankan lengkap dengan urutan start
  - [ ] Port untuk setiap service
  - [ ] Variabel ENV yang perlu diset
  - [ ] Section "Tim & Pembagian Tugas" dengan nama dan NIM
  - [ ] Ringkasan endpoint dengan link ke docs/api/
- [ ] Code lengkap di folder `backend/` dan `frontend/`

---

## 🗄️ 2. Database & Seed

- [ ] **Folder `database/`** ada
- [ ] **`database/schema.sql`** - SQL schema lengkap
- [ ] **`database/seed.sql`** - Sample data
- [ ] **`database/README.md`** - Instruksi import/run
- [ ] **`backend/init_db.py`** - Script Python untuk init database
- [ ] Database menggunakan MySQL (sudah sesuai)

**Cara test:**
```bash
# Test import schema
mysql -u root -p < database/schema.sql

# Test import seed
mysql -u root -p pastry_db < database/seed.sql

# ATAU test script Python
python backend/init_db.py
```

---

## 📡 3. Dokumentasi API

### Option A: Postman (Sudah dipilih)

- [ ] **`documentation/Pastry_API.postman_collection.json`** - Collection lengkap
- [ ] **`documentation/Pastry_API.postman_environment.json`** - Environment file
- [ ] Collection berisi semua endpoint:
  - [ ] Authentication (Login Customer, Login Admin)
  - [ ] Customers (GET, POST, PUT, DELETE)
  - [ ] Restaurants (GET, POST, PUT, DELETE)
  - [ ] Menus (GET, POST, PUT, DELETE)
  - [ ] Orders (GET, POST, PATCH status, DELETE)
- [ ] Setiap endpoint memiliki contoh request/response
- [ ] **`docs/api/ENDPOINTS.md`** - Dokumentasi lengkap semua endpoint
- [ ] **`docs/api/EXAMPLES.md`** - Contoh request/response untuk setiap endpoint kunci

**Cara test:**
1. Import collection ke Postman
2. Import environment
3. Test semua endpoint
4. Pastikan semua request/response benar

---

## 🎨 4. Web Frontend

- [ ] **`frontend/index.html`** - Customer interface
- [ ] **`frontend/admin.html`** - Admin dashboard
- [ ] Frontend memanggil API Gateway (bukan langsung ke service)
- [ ] Minimal 2 halaman yang menampilkan data dari ≥2 service:
  - [ ] Customer Interface: Menu (Menu Service) + Orders (Order Service)
  - [ ] Admin Dashboard: Orders (Order Service) + Customer Info (Customer Service)
- [ ] Instruksi build/run ada di README.md

**Cara test:**
```bash
cd frontend
python -m http.server 8000
# Buka http://localhost:8000/index.html
# Buka http://localhost:8000/admin.html
# Test semua fitur
```

---

## 🎬 5. Video Demo (≤10 menit)

- [ ] **`video/SCRIPT.md`** - Script video sudah ada
- [ ] **`video/link.txt`** - Berisi URL video (YouTube/Drive)
- [ ] Video berisi:
  - [ ] Pengenalan & arsitektur
  - [ ] Run komponen (gateway → services → frontend)
  - [ ] Demo inter-service via gateway
  - [ ] Dokumentasi API (Postman)
  - [ ] Frontend konsumsi gateway
- [ ] Durasi 8-10 menit
- [ ] Video sudah diupload dan accessible

**Cara test:**
- Buka URL di video/link.txt
- Pastikan video bisa diputar
- Pastikan semua bagian ada di video

---

## 📸 6. Bukti Pengujian

### Folder `screenshots/` dengan:

#### A. Postman Screenshots (6 files)
- [ ] `postman-collection.png` - Overview collection
- [ ] `postman-login.png` - Login request & response
- [ ] `postman-menus.png` - Get menus
- [ ] `postman-create-order.png` - Create order
- [ ] `postman-orders.png` - Get orders (dengan Authorization header)
- [ ] `postman-update-status.png` - Update status

#### B. Health Check (4 files)
- [ ] `health-gateway.png` - API Gateway health
- [ ] `health-customer.png` - Customer Service health
- [ ] `health-menu.png` - Menu Service health
- [ ] `health-order.png` - Order Service health

#### C. Frontend (4 files)
- [ ] `frontend-customer-menu.png` - Customer menu page
- [ ] `frontend-customer-orders.png` - Customer orders
- [ ] `frontend-admin-orders.png` - Admin orders table
- [ ] `frontend-admin-details.png` - Admin order details modal

**Total: 14 screenshots**

**Cara test:**
- Buka folder screenshots/
- Pastikan semua file ada
- Pastikan semua screenshot jelas dan readable

---

## 🔍 Final Verification

Sebelum submit, pastikan:

### Code & Documentation
- [ ] Semua service bisa dijalankan
- [ ] Database bisa diinisialisasi
- [ ] Frontend bisa diakses
- [ ] Semua endpoint tested dan working
- [ ] README.md lengkap dan jelas

### Files Structure
- [ ] Folder structure sesuai requirement
- [ ] Semua file ada di tempatnya
- [ ] Tidak ada file yang tidak perlu

### Testing
- [ ] Semua fitur tested
- [ ] Tidak ada error yang blocking
- [ ] Screenshot sudah diambil
- [ ] Video sudah dibuat

---

## 📦 Struktur Final yang Harus Ada

```
PastryApp/
├── README.md                          ✅
├── SUBMISSION_GUIDE.md                ✅
├── SUBMISSION_CHECKLIST.md            ✅ (file ini)
├── backend/                           ✅
│   ├── api_gateway/
│   ├── services/
│   ├── init_db.py
│   └── requirements.txt
├── frontend/                          ✅
│   ├── index.html
│   └── admin.html
├── database/                          ✅
│   ├── schema.sql
│   ├── seed.sql
│   └── README.md
├── documentation/                     ✅
│   ├── Pastry_API.postman_collection.json
│   └── Pastry_API.postman_environment.json
├── docs/                              ✅
│   └── api/
│       ├── ENDPOINTS.md
│       └── EXAMPLES.md
├── screenshots/                        ⚠️ (perlu diambil)
│   ├── README.md
│   ├── postman-*.png (6 files)
│   ├── health-*.png (4 files)
│   └── frontend-*.png (4 files)
└── video/                             ⚠️ (perlu dibuat)
    ├── SCRIPT.md
    └── link.txt
```

---

## 🚀 Quick Start untuk Submission

1. **Update README.md:**
   - Tambahkan section "Tim & Pembagian Tugas"
   - Pastikan semua info lengkap

2. **Ambil Screenshots:**
   - Ikuti panduan di `screenshots/README.md`
   - Ambil semua 14 screenshots

3. **Buat Video:**
   - Ikuti script di `video/SCRIPT.md`
   - Record 8-10 menit
   - Upload dan simpan URL

4. **Final Check:**
   - Gunakan checklist ini
   - Pastikan semua ✅

---

**Selamat menyiapkan submission! 🎉**

