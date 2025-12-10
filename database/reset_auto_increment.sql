-- ============================================
-- Reset AUTO_INCREMENT untuk semua tabel
-- ============================================
-- Script ini akan reset AUTO_INCREMENT ke 1
-- untuk semua tabel di database pastry_db
-- ============================================

USE pastry_db;

-- Reset AUTO_INCREMENT untuk tabel orders
ALTER TABLE orders AUTO_INCREMENT = 1;

-- Reset AUTO_INCREMENT untuk tabel order_items
ALTER TABLE order_items AUTO_INCREMENT = 1;

-- Reset AUTO_INCREMENT untuk tabel customers
ALTER TABLE customers AUTO_INCREMENT = 1;

-- Reset AUTO_INCREMENT untuk tabel restaurants
ALTER TABLE restaurants AUTO_INCREMENT = 1;

-- Reset AUTO_INCREMENT untuk tabel menu_items
ALTER TABLE menu_items AUTO_INCREMENT = 1;

-- ============================================
-- Catatan:
-- - Script ini akan reset AUTO_INCREMENT ke 1
-- - Pastikan semua data sudah dihapus sebelum menjalankan script ini
-- - Jika masih ada data, ID berikutnya akan tetap melanjutkan dari nilai terakhir
-- ============================================

