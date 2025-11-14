# 🎯 Panduan Demo Inter-Service via Gateway

## 📖 Maksud "Demo Inter-Service via Gateway"

**Inter-Service Communication** adalah komunikasi antara microservices. Dalam proyek ini, yang perlu didemonstrasikan adalah:

1. **Client → API Gateway → Service**: Semua request dari frontend/client harus melalui API Gateway
2. **Service → Service**: Order Service (Consumer) memanggil Customer Service dan Menu Service (Providers) untuk validasi

---

## 🎬 Cara Mendemonstrasikan (Step-by-Step)

### **Step 1: Login sebagai Customer → Dapat JWT Token**

**Tujuan:** Menunjukkan bahwa semua request harus melalui API Gateway, dan Gateway menangani authentication.

**Cara:**
1. Buka **Postman**
2. Buat request baru: `POST http://localhost:5000/api/login`
3. Body (JSON):
   ```json
   {
     "username": "customer",
     "password": "iamcustomer"
   }
   ```
4. Klik **Send**
5. **Tunjukkan response:**
   ```json
   {
     "access_token": "eyJ0eXAi...",
     "token_type": "Bearer",
     "expires_in": 86400,
     "username": "customer",
     "role": "customer"
   }
   ```
6. **Copy token** untuk step berikutnya

**Yang Ditunjukkan:**
- ✅ Request ke API Gateway (port 5000), bukan langsung ke service
- ✅ Gateway menangani authentication dan return JWT token
- ✅ Token akan digunakan untuk request berikutnya

---

### **Step 2: Browse Menu (Panggil Menu Service via Gateway)**

**Tujuan:** Menunjukkan bahwa request ke Menu Service harus melalui API Gateway.

**Cara:**
1. Buat request baru: `GET http://localhost:5000/api/menus`
2. **Headers:**
   ```
   Authorization: Bearer <token_dari_step_1>
   ```
3. Klik **Send**
4. **Tunjukkan response:** List menu items dari Menu Service

**Yang Ditunjukkan:**
- ✅ Request ke API Gateway (`/api/menus`), bukan langsung ke Menu Service (`http://localhost:5003/menus`)
- ✅ Gateway forward request ke Menu Service
- ✅ Gateway return response dari Menu Service ke client
- ✅ JWT token digunakan untuk authorization

**Catatan Penting:**
- ❌ **JANGAN** tunjukkan request langsung ke `http://localhost:5003/menus` (ini salah!)
- ✅ **HARUS** tunjukkan request ke `http://localhost:5000/api/menus` (melalui Gateway)

---

### **Step 3: Place Order (Order Service Memanggil Customer & Menu Service)**

**Tujuan:** Menunjukkan **inter-service communication** - Order Service (Consumer) memanggil Customer Service dan Menu Service (Providers) untuk validasi.

**Cara:**

#### 3.1. Siapkan Request Create Order

1. Buat request baru: `POST http://localhost:5000/api/orders`
2. **Headers:**
   ```
   Authorization: Bearer <token_dari_step_1>
   Content-Type: application/json
   ```
3. **Body (JSON):**
   ```json
   {
     "customer_id": 1,
     "customer_name": "John Doe",
     "customer_email": "john@example.com",
     "customer_phone": "081234567890",
     "delivery_address": "Jl. Contoh No. 123",
     "payment_method": "cash",
     "items": [
       {
         "menu_id": 1,
         "quantity": 2,
         "price": 40000
       },
       {
         "menu_id": 2,
         "quantity": 1,
         "price": 35000
       }
     ],
     "total_price": 75000,
     "tax": 3750
   }
   ```

#### 3.2. Tunjukkan Inter-Service Communication

**SEBELUM klik Send, jelaskan:**

> "Saat saya klik Send, yang terjadi adalah:
> 
> 1. Request dikirim ke **API Gateway** (`/api/orders`)
> 2. Gateway forward ke **Order Service** (`/orders`)
> 3. **Order Service** akan memvalidasi:
>    - Customer ID dengan memanggil **Customer Service**: `GET /customers/1`
>    - Menu items dengan memanggil **Menu Service**: `GET /menus/1` dan `GET /menus/2`
> 4. Jika semua valid, Order Service insert order ke database
> 5. Response dikembalikan melalui Gateway ke client"

#### 3.3. Tunjukkan Terminal Logs

**Saat klik Send, tunjukkan terminal windows:**

**Terminal Order Service:**
- Akan muncul log bahwa Order Service memanggil Customer Service dan Menu Service
- Atau bisa tunjukkan error jika service tidak running

**Terminal Customer Service:**
- Akan menerima request `GET /customers/1` dari Order Service

**Terminal Menu Service:**
- Akan menerima request `GET /menus/1` dan `GET /menus/2` dari Order Service

#### 3.4. Tunjukkan Response

**Response yang berhasil:**
```json
{
  "id": 1,
  "message": "Order created successfully",
  "status": "on_process"
}
```

**Yang Ditunjukkan:**
- ✅ Order berhasil dibuat
- ✅ Order Service (Consumer) berhasil memanggil Customer Service dan Menu Service (Providers)
- ✅ Ini adalah contoh **inter-service communication** dalam microservices

---

### **Step 4: Tunjukkan Order Berhasil Dibuat**

**Cara:**
1. Buat request baru: `GET http://localhost:5000/api/orders`
2. **Headers:**
   ```
   Authorization: Bearer <token_dari_step_1>
   ```
3. Klik **Send**
4. **Tunjukkan response:** List orders termasuk order yang baru dibuat

**Atau bisa tunjukkan di Frontend:**
1. Buka browser: `http://localhost:8000/index.html`
2. Login sebagai customer
3. Tunjukkan order history
4. Order yang baru dibuat akan muncul di list

---

## 🎥 Script untuk Video (Narasi)

> "Sekarang saya akan mendemonstrasikan komunikasi inter-service melalui API Gateway.
> 
> **Step 1: Login**
> [Tunjukkan request login di Postman]
> Saya login sebagai customer untuk mendapatkan JWT token. Request ini dikirim ke API Gateway, bukan langsung ke service.
> 
> **Step 2: Get Menus**
> [Tunjukkan request GET /api/menus]
> Request ini juga melalui API Gateway. Gateway akan forward ke Menu Service dan return response.
> 
> **Step 3: Create Order**
> [Tunjukkan request POST /api/orders]
> Ini adalah bagian penting. Saat membuat order:
> - Request dikirim ke API Gateway
> - Gateway forward ke Order Service
> - **Order Service akan memanggil Customer Service dan Menu Service untuk validasi**
> [Tunjukkan terminal logs jika memungkinkan]
> - Jika semua valid, order berhasil dibuat
> 
> Ini menunjukkan **inter-service communication** - Order Service (Consumer) memanggil Customer Service dan Menu Service (Providers).
> 
> **Step 4: Verify Order**
> [Tunjukkan GET /api/orders atau frontend]
> Order berhasil dibuat dan muncul di list."

---

## ✅ Checklist untuk Demo

- [ ] Semua service sudah running (API Gateway, Customer Service, Menu Service, Order Service)
- [ ] Database sudah terinisialisasi dengan sample data
- [ ] Postman sudah dibuka dan collection sudah diimport
- [ ] Token dari login sudah disiapkan
- [ ] Terminal windows sudah disiapkan untuk menunjukkan logs (opsional)
- [ ] Frontend sudah dibuka untuk verifikasi (opsional)

---

## ⚠️ Tips Penting

1. **Jangan tunjukkan request langsung ke service** (misalnya `http://localhost:5003/menus`)
   - ✅ Benar: `http://localhost:5000/api/menus` (melalui Gateway)
   - ❌ Salah: `http://localhost:5003/menus` (langsung ke service)

2. **Tunjukkan bahwa Order Service memanggil service lain**
   - Bisa dengan terminal logs
   - Atau jelaskan secara verbal
   - Atau tunjukkan sequence diagram di README

3. **Pastikan semua service running**
   - Jika Customer Service atau Menu Service tidak running, order creation akan gagal
   - Ini justru bagus untuk menunjukkan dependency antar service

4. **Gunakan data yang valid**
   - Pastikan customer_id dan menu_id yang digunakan ada di database
   - Cek di `init_db.py` atau database untuk ID yang valid

---

## 📊 Diagram yang Bisa Ditunjukkan

Saat demo, bisa tunjukkan sequence diagram dari README.md:

```
Frontend Client → API Gateway → Order Service → Customer Service
                                      ↓
                                   Menu Service
                                      ↓
                                    Database
```

Ini membantu menjelaskan flow inter-service communication.

---

**Intinya:** Demo ini menunjukkan bahwa:
1. ✅ Semua request client harus melalui API Gateway
2. ✅ Order Service (Consumer) memanggil Customer Service dan Menu Service (Providers) untuk validasi
3. ✅ Ini adalah contoh inter-service communication dalam microservices architecture

