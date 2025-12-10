# 🗄️ Database Setup Guide

Panduan untuk setup database Pastry Delivery System menggunakan **Database-Per-Service** pattern.

## 📋 Prerequisites

- MySQL Server 5.7+ atau MariaDB 10.2+
- MySQL client atau phpMyAdmin

## 🏗️ Architecture: Database-Per-Service

Sistem ini menggunakan **Database-Per-Service** pattern, dimana setiap microservice memiliki database sendiri:

- **customer_db** → Customer Service
- **restaurant_db** → Restaurant Service  
- **menu_db** → Menu Service
- **order_db** → Order Service

### Benefits:
- ✅ Service independence
- ✅ Data isolation
- ✅ Independent scaling
- ✅ Technology diversity (dapat menggunakan DB berbeda per service)

## 🚀 Cara Setup Database

### Metode 1: Menggunakan Script Python (Recommended)

**Paling mudah dan otomatis:**

```bash
# 1. Pastikan MySQL service running
# 2. Konfigurasi .env file di backend/.env
# 3. Jalankan script:
cd backend
python init_db.py
```

Script ini akan:
- ✅ Membuat 4 database terpisah
- ✅ Membuat semua tabel untuk setiap service
- ✅ Insert sample data
- ✅ Menampilkan status sukses

### Metode 2: Menggunakan SQL Files Manual

**Jika ingin import manual:**

#### Step 1: Import Schemas

```bash
# Import semua schema:
mysql -u root -p < database/schema_customer.sql
mysql -u root -p < database/schema_restaurant.sql
mysql -u root -p < database/schema_menu.sql
mysql -u root -p < database/schema_order.sql
```

#### Step 2: Import Seed Data

```bash
# Import seed data:
mysql -u root -p < database/seed_customer.sql
mysql -u root -p < database/seed_restaurant.sql
mysql -u root -p < database/seed_menu.sql
```

### Metode 3: Menggunakan phpMyAdmin

1. Buka phpMyAdmin (http://localhost/phpmyadmin)
2. Klik tab "SQL"
3. Import setiap file schema dan seed secara berurutan

## 📊 Database Structure

### customer_db (Customer Service)

**Tables:**
- `customers` - Data pelanggan

**Schema:**
```sql
customers (
    id, name, email, phone, created_at
)
```

### restaurant_db (Restaurant Service)

**Tables:**
- `restaurants` - Data restoran

**Schema:**
```sql
restaurants (
    id, name, location, created_at
)
```

### menu_db (Menu Service)

**Tables:**
- `menu_items` - Menu makanan/minuman

**Schema:**
```sql
menu_items (
    id, restaurant_id, name, price, description, created_at
)
```

**Note:** `restaurant_id` disimpan sebagai reference, tapi tidak ada FK constraint (database-per-service pattern).

### order_db (Order Service)

**Tables:**
- `orders` - Data pesanan
- `order_items` - Item-item dalam pesanan

**Schema:**
```sql
orders (
    id, customer_id, customer_username, customer_name,
    customer_email, customer_phone, delivery_address,
    payment_method, total_price, tax, status, created_at, updated_at
)

order_items (
    id, order_id, menu_id, quantity, price, created_at
)
```

**Note:** 
- `customer_id` dan `menu_id` disimpan sebagai reference, tapi tidak ada FK constraint ke database lain
- Validasi dilakukan via API calls ke service lain
- `order_id` tetap memiliki FK constraint karena dalam database yang sama

## 🔧 Configuration

Pastikan file `backend/.env` sudah dikonfigurasi:

```env
# MySQL Connection (shared)
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_PORT=3306

# Database Names (Database-Per-Service)
CUSTOMER_DB_NAME=customer_db
RESTAURANT_DB_NAME=restaurant_db
MENU_DB_NAME=menu_db
ORDER_DB_NAME=order_db
```

## ✅ Verification

Setelah setup, verifikasi dengan:

```sql
-- Check all databases exist
SHOW DATABASES LIKE 'customer_db';
SHOW DATABASES LIKE 'restaurant_db';
SHOW DATABASES LIKE 'menu_db';
SHOW DATABASES LIKE 'order_db';

-- Check customer_db tables
USE customer_db;
SHOW TABLES;
SELECT * FROM customers;

-- Check restaurant_db tables
USE restaurant_db;
SHOW TABLES;
SELECT * FROM restaurants;

-- Check menu_db tables
USE menu_db;
SHOW TABLES;
SELECT * FROM menu_items;

-- Check order_db tables
USE order_db;
SHOW TABLES;
SELECT * FROM orders;
SELECT * FROM order_items;
```

## 🔄 Data Relationships (Cross-Service)

Karena menggunakan database-per-service, relationships di-handle via:

1. **API Calls**: Services memanggil service lain untuk validasi
   - Order Service → Customer Service (validate customer)
   - Order Service → Menu Service (validate menu item, fetch menu name)

2. **Denormalization**: Data penting disimpan di service yang membutuhkan
   - Order Service menyimpan `customer_name`, `customer_email`, dll (denormalized)
   - Order Service menyimpan `menu_id` dan fetch `menu_name` via API saat dibutuhkan

## 🐛 Troubleshooting

### Error: "Access denied"
- Pastikan MySQL user dan password benar
- Pastikan user memiliki privilege CREATE DATABASE

### Error: "Table already exists"
- Database sudah pernah dibuat
- Hapus database dulu: `DROP DATABASE customer_db;` (dan database lainnya)
- Atau gunakan `CREATE TABLE IF NOT EXISTS` (sudah ada di schema files)

### Error: "Foreign key constraint fails"
- Dengan database-per-service, FK constraints ke database lain sudah dihapus
- Hanya FK dalam database yang sama (order_items → orders) yang masih ada
- Validasi cross-service dilakukan via API calls

### Service tidak bisa connect ke database
- Pastikan nama database di `.env` sesuai dengan yang dibuat
- Check: `CUSTOMER_DB_NAME`, `RESTAURANT_DB_NAME`, `MENU_DB_NAME`, `ORDER_DB_NAME`

## 📝 Notes

- Database menggunakan charset `utf8mb4` untuk support emoji
- Price menggunakan tipe `INT` (bukan DECIMAL) untuk efisiensi
- Timestamps otomatis dengan `CURRENT_TIMESTAMP`
- Foreign key constraints hanya untuk relationships dalam database yang sama
- Cross-database relationships di-handle via API calls (service-to-service communication)

## 🔄 Migration dari Shared Database

Jika sebelumnya menggunakan shared database (`pastry_db`), migrasi data:

1. Export data dari `pastry_db`
2. Import ke database masing-masing:
   - `customers` → `customer_db`
   - `restaurants` → `restaurant_db`
   - `menu_items` → `menu_db`
   - `orders`, `order_items` → `order_db`
