-- ============================================
-- Restaurant Service - Seed Data
-- ============================================
-- This file contains sample data for testing
-- Run after schema_restaurant.sql
-- ============================================

USE restaurant_db;

-- ============================================
-- Seed: Restaurants
-- ============================================
INSERT INTO restaurants (name, location) VALUES
('Pastry', 'Jakarta, Indonesia')
ON DUPLICATE KEY UPDATE name=name;

-- ============================================
-- End of Seed Data
-- ============================================

