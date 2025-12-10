-- ============================================
-- Customer Service - Seed Data
-- ============================================
-- This file contains sample data for testing
-- Run after schema_customer.sql
-- ============================================

USE customer_db;

-- ============================================
-- Seed: Customers
-- ============================================
INSERT INTO customers (name, email, phone) VALUES
('John Doe', 'john@example.com', '081234567890'),
('Jane Smith', 'jane@example.com', '082345678901')
ON DUPLICATE KEY UPDATE name=name;

-- ============================================
-- End of Seed Data
-- ============================================

