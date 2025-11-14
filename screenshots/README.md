# 📸 Screenshots Guide

Panduan untuk mengambil screenshot bukti pengujian.

---

## 📋 Checklist Screenshots

### A. Postman Collection (6 screenshots)

- [ ] **postman-collection.png** - Overview semua folder dan endpoint
- [ ] **postman-login.png** - Login request & response dengan token
- [ ] **postman-menus.png** - Get menus request & response
- [ ] **postman-create-order.png** - Create order request & response
- [ ] **postman-orders.png** - Get orders request & response (dengan Authorization header)
- [ ] **postman-update-status.png** - Update order status request & response

### B. Health Check Endpoints (4 screenshots)

- [ ] **health-gateway.png** - API Gateway health check
- [ ] **health-customer.png** - Customer Service health check
- [ ] **health-menu.png** - Menu Service health check
- [ ] **health-order.png** - Order Service health check

### C. Frontend (4 screenshots)

- [ ] **frontend-customer-menu.png** - Customer interface menampilkan menu
- [ ] **frontend-customer-orders.png** - Customer interface order history
- [ ] **frontend-admin-orders.png** - Admin dashboard orders table
- [ ] **frontend-admin-details.png** - Admin dashboard order details modal

---

## 📸 Cara Mengambil Screenshot

### Postman Screenshots

1. Buka Postman
2. Import collection: `documentation/Pastry_API.postman_collection.json`
3. Untuk setiap screenshot:
   - Pilih request yang sesuai
   - Klik "Send"
   - Tunggu response muncul
   - Tekan `Print Screen` atau gunakan Snipping Tool (Windows) / Cmd+Shift+4 (Mac)
   - Simpan dengan nama yang sesuai

**Tips:**
- Pastikan request dan response terlihat jelas
- Untuk postman-orders.png, pastikan Authorization header terlihat
- Crop screenshot agar fokus pada bagian penting

### Health Check Screenshots

1. Buka browser
2. Akses URL health check:
   - http://localhost:5050/health (API Gateway)
   - http://localhost:5001/health (Customer Service)
   - http://localhost:5003/health (Menu Service)
   - http://localhost:5004/health (Order Service)
3. Screenshot halaman response

**Jika tidak ada endpoint /health:**
- Screenshot terminal yang menunjukkan service running
- Atau screenshot response dari endpoint lain yang menunjukkan service aktif

### Frontend Screenshots

1. Buka browser
2. Akses frontend: http://localhost:8000/index.html atau admin.html
3. Untuk setiap screenshot:
   - Navigate ke halaman/fitur yang sesuai
   - Pastikan konten terlihat jelas
   - Tekan F11 untuk fullscreen (opsional)
   - Tekan `Print Screen` atau gunakan Snipping Tool
   - Simpan dengan nama yang sesuai

**Tips:**
- Pastikan tidak ada DevTools terbuka (kecuali perlu)
- Pastikan konten terlihat jelas dan readable
- Untuk modal, pastikan modal terbuka dan terlihat jelas

---

## 🎨 Tips Screenshot yang Baik

1. **Resolusi:**
   - Minimal 1920x1080
   - Pastikan text readable

2. **Konten:**
   - Fokus pada bagian penting
   - Crop bagian yang tidak perlu
   - Pastikan semua informasi penting terlihat

3. **Konsistensi:**
   - Gunakan format PNG untuk kualitas lebih baik
   - Nama file konsisten (lowercase, dengan dash)
   - Simpan semua di folder `screenshots/`

4. **Anotasi (Opsional):**
   - Bisa tambahkan arrow atau highlight jika perlu
   - Bisa tambahkan text label jika perlu
   - Gunakan tool seperti Snagit atau Greenshot

---

## 📁 Struktur Folder

```
screenshots/
├── README.md (file ini)
├── postman-collection.png
├── postman-login.png
├── postman-menus.png
├── postman-create-order.png
├── postman-orders.png
├── postman-update-status.png
├── health-gateway.png
├── health-customer.png
├── health-menu.png
├── health-order.png
├── frontend-customer-menu.png
├── frontend-customer-orders.png
├── frontend-admin-orders.png
└── frontend-admin-details.png
```

---

## ✅ Verifikasi Screenshots

Sebelum submit, pastikan:

- [ ] Semua screenshot sudah diambil
- [ ] Semua screenshot jelas dan readable
- [ ] Nama file sesuai checklist
- [ ] Semua screenshot disimpan di folder `screenshots/`
- [ ] Screenshot menunjukkan fitur yang diminta

---

**Selamat mengambil screenshot! 📸**

