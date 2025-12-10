# 🗄️ Database Setup Guide

Panduan untuk setup database Pastry Delivery System.

## 📋 Prerequisites

- MySQL Server 5.7+ atau MariaDB 10.2+
- MySQL client atau phpMyAdmin

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
- ✅ Membuat database `pastry_db`
- ✅ Membuat semua tabel
- ✅ Insert sample data
- ✅ Menampilkan status sukses

### Metode 2: Menggunakan SQL Files Manual

**Jika ingin import manual:**

#### Step 1: Import Schema

```bash
# Via command line:
mysql -u root -p < database/schema.sql

# Atau via MySQL client:
mysql -u root -p
source database/schema.sql
```

#### Step 2: Import Seed Data

```bash
# Via command line:
mysql -u root -p pastry_db < database/seed.sql

# Atau via MySQL client:
mysql -u root -p
USE pastry_db;
source database/seed.sql
```

### Metode 3: Menggunakan phpMyAdmin

1. Buka phpMyAdmin (http://localhost/phpmyadmin)
2. Klik tab "SQL"
3. Copy isi `database/schema.sql`
4. Paste dan klik "Go"
5. Ulangi untuk `database/seed.sql`

## 📊 Database Structure

### Tables

1. **customers** - Data pelanggan
2. **restaurants** - Data restoran
3. **menu_items** - Menu makanan/minuman
4. **orders** - Data pesanan
5. **order_items** - Item-item dalam pesanan

### Relationships

```
restaurants (1) ──< menu_items (many)
customers (1) ──< orders (many)
orders (1) ──< order_items (many)
menu_items (1) ──< order_items (many)
```

## 🔧 Configuration

Pastikan file `backend/.env` sudah dikonfigurasi:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=pastry_db
MYSQL_PORT=3306
```

## ✅ Verification

Setelah setup, verifikasi dengan:

```sql
-- Check database exists
SHOW DATABASES LIKE 'pastry_db';

-- Check tables
USE pastry_db;
SHOW TABLES;

-- Check sample data
SELECT * FROM customers;
SELECT * FROM restaurants;
SELECT * FROM menu_items;
```

## 🐛 Troubleshooting

### Error: "Access denied"
- Pastikan MySQL user dan password benar
- Pastikan user memiliki privilege CREATE DATABASE

### Error: "Table already exists"
- Database sudah pernah dibuat
- Hapus database dulu: `DROP DATABASE pastry_db;`
- Atau gunakan `CREATE TABLE IF NOT EXISTS` (sudah ada di schema.sql)

### Error: "Foreign key constraint fails"
- Pastikan import schema.sql dulu sebelum seed.sql
- Pastikan data restaurants ada sebelum menu_items
- Pastikan data customers ada sebelum orders

## 📝 Notes

- Database menggunakan charset `utf8mb4` untuk support emoji
- Semua foreign keys menggunakan `ON DELETE CASCADE`
- Price menggunakan tipe `INT` (bukan DECIMAL) untuk efisiensi
- Timestamps otomatis dengan `CURRENT_TIMESTAMP`

