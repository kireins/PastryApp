-- ============================================
-- Menu Service - Seed Data
-- ============================================
-- This file contains sample data for testing
-- Run after schema_menu.sql
-- ============================================

USE menu_db;

-- ============================================
-- Seed: Menu Items
-- ============================================
INSERT INTO menu_items (restaurant_id, name, price, description) VALUES
(1, 'Chocolate Croissant', 35000, 'Delicious chocolate filled croissant'),
(1, 'Strawberry Tart', 45000, 'Fresh strawberry tart with cream'),
(1, 'Vanilla Donut', 25000, 'Soft vanilla donut with glaze'),
(1, 'Matcha Cake', 55000, 'Premium matcha cake')
ON DUPLICATE KEY UPDATE name=name;

-- ============================================
-- End of Seed Data
-- ============================================

