-- ============================================
-- Restaurant Service Database Schema
-- ============================================
-- Database: restaurant_db
-- Created: 2025
-- ============================================

-- Create Database
CREATE DATABASE IF NOT EXISTS restaurant_db;
USE restaurant_db;

-- ============================================
-- Table: restaurants
-- Description: Stores restaurant information
-- ============================================
CREATE TABLE IF NOT EXISTS restaurants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- End of Schema
-- ============================================

