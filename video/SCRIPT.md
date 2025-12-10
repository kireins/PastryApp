# 🎬 Video Demo Script

Script untuk video demo Pastry Delivery System (8-10 menit).

---

## 📋 Persiapan Sebelum Recording

1. ✅ Semua service sudah running
2. ✅ Database sudah terinisialisasi
3. ✅ Postman collection sudah diimport
4. ✅ Browser sudah dibuka dengan frontend
5. ✅ Terminal windows sudah disiapkan

---

## 🎥 Script Video (8-10 menit)

### **Bagian 1: Pengenalan & Arsitektur** (1-2 menit)

**[Scene: Tampilkan README.md atau diagram arsitektur]**

> "Halo, saya akan mendemonstrasikan proyek Pastry Delivery System, sebuah aplikasi food delivery berbasis microservices.
> 
> Arsitektur sistem ini menggunakan pattern Client → API Gateway → Services → Database.
> 
> [Tunjukkan diagram/README]
> 
> Kami memiliki:
> - 1 API Gateway yang menangani routing dan authentication
> - 4 Microservices: Customer Service, Restaurant Service, Menu Service, dan Order Service
> - 1 Database MySQL untuk menyimpan data
> - 2 Frontend: Customer Interface dan Admin Dashboard
> 
> Semua komunikasi client ke services harus melalui API Gateway, tidak langsung ke service."

---

### **Bagian 2: Menjalankan Komponen** (2-3 menit)

**[Scene: Tunjukkan terminal windows dengan services running]**

> "Sekarang saya akan menunjukkan cara menjalankan semua komponen.
> 
> [Tunjukkan terminal 1 - API Gateway]
> Ini adalah API Gateway yang berjalan di port 5050. Gateway ini menangani JWT authentication dan routing ke services.
> 
> [Tunjukkan terminal 2 - Customer Service]
> Customer Service di port 5001, menangani data pelanggan.
> 
> [Tunjukkan terminal 3 - Menu Service]
> Menu Service di port 5003, menangani data menu.
> 
> [Tunjukkan terminal 4 - Order Service]
> Order Service di port 5004, menangani pesanan dan memvalidasi dengan service lain.
> 
> [Tunjukkan database]
> Database MySQL sudah terinisialisasi dengan schema dan sample data.
> 
> [Tunjukkan browser - Frontend]
> Frontend berjalan di port 8000, siap digunakan."

---

### **Bagian 3: Demo Inter-Service via Gateway** (2-3 menit)

**[Scene: Gunakan Postman untuk demo API]**

> "Sekarang saya akan mendemonstrasikan komunikasi inter-service melalui API Gateway.
> 
> [Buka Postman]
> 
> **Step 1: Login sebagai Customer**
> [Tunjukkan request login]
> Saya akan login sebagai customer untuk mendapatkan JWT token.
> [Klik Send, tunjukkan response dengan token]
> Berhasil! Saya mendapat JWT token yang akan digunakan untuk request selanjutnya.
> 
> **Step 2: Get Menus**
> [Tunjukkan request GET /api/menus]
> Request ini akan di-routing oleh Gateway ke Menu Service.
> [Klik Send, tunjukkan response]
> Menu Service mengembalikan daftar menu yang tersedia.
> 
> **Step 3: Create Order**
> [Tunjukkan request POST /api/orders dengan token]
> Saat membuat order, Order Service akan memvalidasi:
> - Customer ID dengan Customer Service
> - Menu items dengan Menu Service
> [Klik Send, tunjukkan response]
> Order berhasil dibuat! Ini menunjukkan Order Service (Consumer) berhasil memanggil Customer Service dan Menu Service (Providers)."

---

### **Bagian 4: Dokumentasi API** (1-2 menit)

**[Scene: Tunjukkan Postman Collection]**

> "Sekarang saya akan menunjukkan dokumentasi API.
> 
> [Tunjukkan Postman Collection]
> Ini adalah Postman Collection yang berisi semua endpoint API.
> 
> [Expand folder Authentication]
> Folder Authentication berisi endpoint login untuk customer dan admin.
> 
> [Expand folder Customers]
> Folder Customers berisi CRUD operations untuk customer.
> 
> [Expand folder Menus]
> Folder Menus berisi operasi untuk menu items.
> 
> [Expand folder Orders]
> Folder Orders berisi operasi untuk orders, termasuk update status.
> 
> [Tunjukkan salah satu request dengan contoh]
> Setiap endpoint memiliki contoh request dan response yang jelas.
> 
> Dokumentasi lengkap juga tersedia di folder docs/api/ dengan penjelasan detail setiap endpoint."

---

### **Bagian 5: Frontend Konsumsi Gateway** (2 menit)

**[Scene: Tunjukkan browser dengan frontend]**

> "Sekarang saya akan menunjukkan frontend yang mengonsumsi API Gateway.
> 
> **Customer Interface:**
> [Buka index.html]
> 
> [Tunjukkan login]
> Customer login menggunakan API Gateway endpoint /api/login.
> 
> [Tunjukkan menu browsing]
> Menu items ditampilkan dengan memanggil /api/menus melalui Gateway.
> 
> [Tunjukkan add to cart]
> Customer dapat menambahkan item ke cart.
> 
> [Tunjukkan place order]
> Saat place order, frontend memanggil /api/orders melalui Gateway.
> Order Service kemudian memvalidasi dengan Customer Service dan Menu Service.
> 
> [Tunjukkan order history]
> Order history ditampilkan dengan memanggil /api/orders melalui Gateway.
> 
> **Admin Dashboard:**
> [Buka admin.html]
> 
> [Login sebagai admin]
> Admin login dan otomatis redirect ke dashboard.
> 
> [Tunjukkan orders table]
> Dashboard menampilkan semua orders dengan memanggil /api/orders melalui Gateway.
> 
> [Tunjukkan update status]
> Admin dapat update status order dengan memanggil /api/orders/{id}/status.
> 
> [Tunjukkan order details]
> Klik View untuk melihat detail order lengkap dengan items.
> 
> Semua request frontend ke services selalu melalui API Gateway, tidak langsung ke service."

---

### **Penutup** (30 detik)

> "Demikian demonstrasi Pastry Delivery System.
> 
> Fitur utama yang telah ditunjukkan:
> - Arsitektur microservices dengan API Gateway
> - Inter-service communication (Consumer-Provider pattern)
> - JWT authentication dengan role-based access
> - Frontend yang mengonsumsi API melalui Gateway
> - Dokumentasi API lengkap
> 
> Terima kasih!"

---

## 📝 Tips Recording

1. **Persiapan:**
   - Pastikan semua service running sebelum mulai
   - Test semua fitur dulu sebelum recording
   - Siapkan script di samping untuk reference

2. **Recording:**
   - Gunakan OBS Studio atau screen recorder
   - Record dengan resolusi minimal 1080p
   - Pastikan suara jelas (gunakan microphone)
   - Jangan terlalu cepat, beri waktu untuk viewer memahami

3. **Editing:**
   - Potong bagian yang tidak perlu
   - Tambahkan text overlay jika perlu (untuk highlight)
   - Pastikan durasi 8-10 menit
   - Tambahkan intro/outro jika mau

4. **Upload:**
   - Upload ke YouTube (set as Unlisted)
   - Atau upload ke Google Drive
   - Simpan URL di file `video/link.txt`

---

## ✅ Checklist Sebelum Recording

- [ ] Semua service running dan tested
- [ ] Database sudah ada data sample
- [ ] Postman collection sudah diimport
- [ ] Frontend bisa diakses
- [ ] Script sudah dipahami
- [ ] Screen recorder siap
- [ ] Microphone tested
- [ ] Browser dan terminal sudah disiapkan

---

**Good luck dengan recording! 🎬**

