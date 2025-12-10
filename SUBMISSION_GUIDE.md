# 📋 Panduan Lengkap Submission Proyek PastryApp

Panduan ini akan membantu Anda menyiapkan semua dokumen dan file yang diperlukan untuk submission.

## ✅ Checklist Submission

- [ ] 1. Code + README.md (root)
- [ ] 2. Database & Seed
- [ ] 3. Dokumentasi API (Postman Collection)
- [ ] 4. Web Frontend sederhana
- [ ] 5. Video demo (≤10 menit)
- [ ] 6. Bukti pengujian (Screenshots)

---

## 1️⃣ Code + README.md (Root)

### File yang sudah ada:
- ✅ `README.md` - Sudah lengkap dengan deskripsi, arsitektur, cara menjalankan
- ✅ Code lengkap di folder `backend/` dan `frontend/`

### Yang perlu ditambahkan ke README.md:

#### A. Anggota & Peran (Tambahkan di README.md)

Tambahkan section ini di README.md:

```markdown
## 👥 Tim & Pembagian Tugas

| Nama Anggota | NIM | Peran | Service/Fitur yang Dikerjakan |
|--------------|-----|-------|------------------------------|
| [Nama 1] | [NIM] | Backend Developer | API Gateway, Customer Service |
| [Nama 2] | [NIM] | Backend Developer | Menu Service, Order Service |
| [Nama 3] | [NIM] | Frontend Developer | Customer Interface (index.html) |
| [Nama 4] | [NIM] | Frontend Developer | Admin Dashboard (admin.html) |
```

**Cara mengisi:**
1. Ganti [Nama], [NIM] dengan data anggota tim
2. Isi kolom "Service/Fitur yang Dikerjakan" sesuai pembagian kerja

#### B. Ringkasan Endpoint (Sudah ada, pastikan lengkap)

Pastikan section "🔌 API Endpoints" di README.md sudah lengkap. Jika belum, tambahkan link ke dokumentasi lengkap:

```markdown
## 🔌 API Endpoints

Ringkasan endpoint tersedia di [docs/api/ENDPOINTS.md](docs/api/ENDPOINTS.md)

Dokumentasi lengkap dengan contoh request/response tersedia di:
- Postman Collection: `documentation/Pastry_API.postman_collection.json`
- Import ke Postman untuk melihat detail lengkap
```

---

## 2️⃣ Database & Seed

### File yang sudah ada:
- ✅ `backend/init_db.py` - Script untuk membuat database dan seed data

### File yang perlu dibuat:

#### A. SQL Schema File

Buat file `database/schema.sql`:

```bash
mkdir -p database
```

Kemudian buat file `database/schema.sql` (akan dibuat otomatis)

#### B. Seed Data File

Buat file `database/seed.sql` (akan dibuat otomatis)

#### C. Instruksi Import Database

Buat file `database/README.md` dengan instruksi:

**Untuk MySQL:**
```bash
# 1. Login ke MySQL
mysql -u root -p

# 2. Import schema
mysql -u root -p < database/schema.sql

# 3. Import seed data
mysql -u root -p pastry_db < database/seed.sql

# ATAU gunakan script Python (lebih mudah):
python backend/init_db.py
```

---

## 3️⃣ Dokumentasi API

### File yang sudah ada:
- ✅ `documentation/Pastry_API.postman_collection.json`

### Yang perlu dilakukan:

#### A. Pastikan Postman Collection Lengkap

1. Buka Postman
2. Import `documentation/Pastry_API.postman_collection.json`
3. Pastikan semua endpoint ada:
   - ✅ Authentication (Login Customer, Login Admin)
   - ✅ Customers (GET, POST, PUT, DELETE)
   - ✅ Restaurants (GET, POST, PUT, DELETE)
   - ✅ Menus (GET, POST, PUT, DELETE)
   - ✅ Orders (GET, POST, PUT, PATCH status, DELETE)

#### B. Buat Postman Environment

Buat file `documentation/Pastry_API.postman_environment.json` (akan dibuat)

#### C. Buat Dokumentasi API Lengkap

Buat folder dan file:
- `docs/api/ENDPOINTS.md` - Dokumentasi lengkap semua endpoint
- `docs/api/EXAMPLES.md` - Contoh request/response untuk setiap endpoint

---

## 4️⃣ Web Frontend

### File yang sudah ada:
- ✅ `frontend/index.html` - Customer interface
- ✅ `frontend/admin.html` - Admin dashboard

### Yang perlu ditambahkan:

#### A. Instruksi Build/Run Frontend

Tambahkan di README.md section "Frontend":

```markdown
## 🎨 Frontend

### Build & Run

Frontend menggunakan HTML/CSS/JavaScript murni, tidak perlu build.

**Cara menjalankan:**

1. **Menggunakan Python HTTP Server:**
```bash
cd frontend
python -m http.server 8000
```

2. **Menggunakan Node.js (jika ada):**
```bash
cd frontend
npx http-server -p 8000
```

3. **Akses:**
- Customer: http://localhost:8000/index.html
- Admin: http://localhost:8000/admin.html

### Fitur Frontend

**Customer Interface (`index.html`):**
- ✅ Memanggil API Gateway (http://localhost:5050/api)
- ✅ Menampilkan data dari Menu Service (menu items)
- ✅ Menampilkan data dari Order Service (order history)
- ✅ Fitur: Login, Browse Menu, Add to Cart, Place Order, View Orders

**Admin Dashboard (`admin.html`):**
- ✅ Memanggil API Gateway (http://localhost:5050/api)
- ✅ Menampilkan data dari Order Service (all orders)
- ✅ Menampilkan data dari Customer Service (customer info)
- ✅ Fitur: Login, View All Orders, Update Status, Delete Orders
```

---

## 5️⃣ Video Demo (≤10 menit)

### Script Video Demo:

**Durasi: 8-10 menit**

#### Bagian 1: Pengenalan & Arsitektur (1-2 menit)
1. Perkenalkan proyek: "Pastry Delivery System"
2. Tunjukkan arsitektur:
   - Client → API Gateway → Services → Database
   - 4 Microservices: Customer, Restaurant, Menu, Order
   - Frontend: Customer & Admin

#### Bagian 2: Menjalankan Komponen (2-3 menit)
1. Tunjukkan cara start services:
   - API Gateway (port 5050)
   - Customer Service (port 5001)
   - Menu Service (port 5003)
   - Order Service (port 5004)
2. Tunjukkan database sudah terinisialisasi
3. Tunjukkan frontend running (port 8000)

#### Bagian 3: Demo Inter-Service via Gateway (2-3 menit)

**Tujuan:** Menunjukkan komunikasi inter-service melalui API Gateway dan service-to-service communication.

**Cara Demo:**

1. **Login sebagai Customer → Dapat JWT Token**
   - Postman: `POST http://localhost:5000/api/login`
   - Body: `{"username": "customer", "password": "iamcustomer"}`
   - **Tunjukkan:** Request ke API Gateway (port 5000), bukan langsung ke service
   - **Tunjukkan:** Response dengan JWT token
   - **Copy token** untuk step berikutnya

2. **Browse Menu (Panggil Menu Service via Gateway)**
   - Postman: `GET http://localhost:5000/api/menus`
   - Headers: `Authorization: Bearer <token>`
   - **Tunjukkan:** Request ke Gateway (`/api/menus`), bukan langsung ke Menu Service
   - **Tunjukkan:** Gateway forward ke Menu Service dan return response
   - **Jangan tunjukkan:** Request langsung ke `http://localhost:5003/menus` (ini salah!)

3. **Place Order (Order Service Memanggil Customer & Menu Service)**
   - Postman: `POST http://localhost:5000/api/orders`
   - Headers: `Authorization: Bearer <token>`
   - Body: Order dengan `customer_id` dan `items` (menu_id)
   - **SEBELUM klik Send, jelaskan:**
     - Request ke API Gateway
     - Gateway forward ke Order Service
     - **Order Service akan memanggil:**
       - Customer Service: `GET /customers/{id}` untuk validasi
       - Menu Service: `GET /menus/{id}` untuk validasi setiap item
   - **Saat klik Send, tunjukkan terminal logs** (jika memungkinkan):
     - Order Service terminal: menunjukkan call ke Customer/Menu Service
     - Customer Service terminal: menerima request dari Order Service
     - Menu Service terminal: menerima request dari Order Service
   - **Tunjukkan:** Response order berhasil dibuat
   - **Ini adalah contoh inter-service communication!**

4. **Tunjukkan Order Berhasil Dibuat**
   - Postman: `GET http://localhost:5000/api/orders` (dengan token)
   - **Atau** tunjukkan di Frontend: `http://localhost:8000/index.html` → Login → Order History
   - Order yang baru dibuat akan muncul di list

**Yang Harus Ditunjukkan:**
- ✅ Semua request client melalui API Gateway (bukan langsung ke service)
- ✅ Order Service (Consumer) memanggil Customer Service dan Menu Service (Providers)
- ✅ Ini adalah contoh **inter-service communication** dalam microservices

**Lihat panduan lengkap:** `DEMO_INTER_SERVICE_GUIDE.md`

#### Bagian 4: Dokumentasi API (1-2 menit)
1. Buka Postman
2. Import collection
3. Tunjukkan beberapa endpoint:
   - Login
   - Get Menus
   - Create Order
   - Get Orders
4. Tunjukkan request/response

#### Bagian 5: Frontend Konsumsi Gateway (1-2 menit)
1. Tunjukkan Customer Interface:
   - Login
   - Browse menu
   - Add to cart
   - Place order
   - View order history
2. Tunjukkan Admin Dashboard:
   - Login
   - View all orders
   - Update status
   - View order details

### Tips Recording:
- Gunakan OBS Studio atau screen recording tool
- Pastikan suara jelas
- Tunjukkan terminal windows untuk services
- Tunjukkan browser untuk frontend
- Tunjukkan Postman untuk API testing

### Upload:
- Upload ke YouTube (unlisted) atau Google Drive
- Simpan URL di file `video/link.txt`

---

## 6️⃣ Bukti Pengujian

### Screenshot yang diperlukan:

#### A. Swagger UI (jika ada) atau Postman

**Screenshot 1: Postman Collection Overview**
- Tunjukkan semua folder dan endpoint
- File: `screenshots/postman-collection.png`

**Screenshot 2: Login Request & Response**
- Tunjukkan request body
- Tunjukkan response dengan token
- File: `screenshots/postman-login.png`

**Screenshot 3: Get Menus Request & Response**
- Tunjukkan request
- Tunjukkan response dengan data menu
- File: `screenshots/postman-menus.png`

**Screenshot 4: Create Order Request & Response**
- Tunjukkan request body lengkap
- Tunjukkan response sukses
- File: `screenshots/postman-create-order.png`

**Screenshot 5: Get Orders Request & Response**
- Tunjukkan request dengan Authorization header
- Tunjukkan response dengan list orders
- File: `screenshots/postman-orders.png`

**Screenshot 6: Update Order Status**
- Tunjukkan PATCH request
- Tunjukkan response sukses
- File: `screenshots/postman-update-status.png`

#### B. Health Check Endpoints

**Screenshot 7: API Gateway Health**
- `http://localhost:5050/health` atau test endpoint
- File: `screenshots/health-gateway.png`

**Screenshot 8: Customer Service Health**
- `http://localhost:5001/health`
- File: `screenshots/health-customer.png`

**Screenshot 9: Menu Service Health**
- `http://localhost:5003/health`
- File: `screenshots/health-menu.png`

**Screenshot 10: Order Service Health**
- `http://localhost:5004/health`
- File: `screenshots/health-order.png`

#### C. Frontend Screenshots

**Screenshot 11: Customer Interface - Menu**
- Tunjukkan menu items ditampilkan
- File: `screenshots/frontend-customer-menu.png`

**Screenshot 12: Customer Interface - Order History**
- Tunjukkan order history
- File: `screenshots/frontend-customer-orders.png`

**Screenshot 13: Admin Dashboard - Orders Table**
- Tunjukkan orders table
- File: `screenshots/frontend-admin-orders.png`

**Screenshot 14: Admin Dashboard - Order Details Modal**
- Tunjukkan modal dengan detail order
- File: `screenshots/frontend-admin-details.png`

### Cara mengambil screenshot:

1. **Postman:**
   - Buka Postman
   - Jalankan request
   - Tekan `Print Screen` atau gunakan Snipping Tool
   - Simpan di folder `screenshots/`

2. **Browser:**
   - Buka halaman
   - Tekan F12 untuk DevTools (opsional, tutup untuk screenshot bersih)
   - Tekan `Print Screen` atau gunakan Snipping Tool
   - Simpan di folder `screenshots/`

3. **Terminal/Command Prompt:**
   - Untuk health check, buka browser dan akses URL
   - Atau screenshot terminal dengan response

---

## 📁 Struktur Folder Final

```
PastryApp/
├── README.md                          # ✅ Sudah ada (perlu update anggota)
├── backend/                           # ✅ Code lengkap
├── frontend/                          # ✅ Code lengkap
├── database/                          # ⚠️ Perlu dibuat
│   ├── schema.sql                     # ⚠️ Perlu dibuat
│   ├── seed.sql                       # ⚠️ Perlu dibuat
│   └── README.md                      # ⚠️ Perlu dibuat
├── documentation/                     # ✅ Sudah ada
│   ├── Pastry_API.postman_collection.json  # ✅ Sudah ada
│   └── Pastry_API.postman_environment.json # ⚠️ Perlu dibuat
├── docs/                              # ⚠️ Perlu dibuat
│   └── api/
│       ├── ENDPOINTS.md               # ⚠️ Perlu dibuat
│       └── EXAMPLES.md                # ⚠️ Perlu dibuat
├── screenshots/                       # ⚠️ Perlu dibuat
│   ├── postman-*.png                  # ⚠️ Perlu diambil
│   ├── health-*.png                    # ⚠️ Perlu diambil
│   └── frontend-*.png                  # ⚠️ Perlu diambil
└── video/                             # ⚠️ Perlu dibuat
    └── link.txt                       # ⚠️ Perlu diisi URL video
```

---

## 🚀 Langkah-langkah Eksekusi

### Step 1: Update README.md
1. Buka `README.md`
2. Tambahkan section "Tim & Pembagian Tugas"
3. Pastikan semua informasi lengkap

### Step 2: Buat Database Files
1. Jalankan script untuk generate SQL files
2. Buat folder `database/`
3. Buat `database/README.md` dengan instruksi

### Step 3: Update Postman Collection
1. Buka Postman
2. Import collection
3. Test semua endpoint
4. Export environment jika perlu
5. Pastikan collection lengkap

### Step 4: Buat Dokumentasi API
1. Buat folder `docs/api/`
2. Buat `ENDPOINTS.md` dengan semua endpoint
3. Buat `EXAMPLES.md` dengan contoh request/response

### Step 5: Ambil Screenshots
1. Buat folder `screenshots/`
2. Ambil semua screenshot sesuai checklist
3. Pastikan jelas dan readable

### Step 6: Buat Video Demo
1. Siapkan script demo
2. Record video (8-10 menit)
3. Upload ke YouTube/Drive
4. Simpan URL di `video/link.txt`

---

## ✅ Final Checklist Sebelum Submit

- [ ] README.md lengkap dengan anggota tim
- [ ] Database schema & seed files ada
- [ ] Postman collection lengkap dan tested
- [ ] Dokumentasi API lengkap di docs/api/
- [ ] Semua screenshot sudah diambil
- [ ] Video demo sudah dibuat dan diupload
- [ ] Semua service bisa dijalankan
- [ ] Frontend bisa diakses dan berfungsi
- [ ] Semua endpoint tested dan working

---

**Selamat menyiapkan submission! 🎉**

