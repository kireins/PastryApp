-- ============================================
-- Menu Service Database Schema
-- ============================================
-- Database: menu_db
-- Created: 2025
-- ============================================

-- Create Database
CREATE DATABASE IF NOT EXISTS menu_db;
USE menu_db;

-- ============================================
-- Table: menu_items
-- Description: Stores menu items for restaurants
-- Note: restaurant_id is stored but FK constraint removed for database-per-service pattern
-- ============================================
CREATE TABLE IF NOT EXISTS menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    restaurant_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_restaurant_id (restaurant_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- End of Schema
-- ============================================

