-- ============================================
-- Pastry Delivery System - Seed Data
-- ============================================
-- This file contains sample data for testing
-- Run after schema.sql
-- ============================================

USE pastry_db;

-- ============================================
-- Seed: Customers
-- ============================================
INSERT INTO customers (name, email, phone) VALUES
('John Doe', 'john@example.com', '081234567890'),
('Jane Smith', 'jane@example.com', '082345678901')
ON DUPLICATE KEY UPDATE name=name;

-- ============================================
-- Seed: Restaurants
-- ============================================
INSERT INTO restaurants (name, location) VALUES
('Pastry', 'Jakarta, Indonesia')
ON DUPLICATE KEY UPDATE name=name;

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

