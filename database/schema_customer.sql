-- ============================================
-- Customer Service Database Schema
-- ============================================
-- Database: customer_db
-- Created: 2025
-- ============================================

-- Create Database
CREATE DATABASE IF NOT EXISTS customer_db;
USE customer_db;

-- ============================================
-- Table: customers
-- Description: Stores customer information
-- ============================================
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- End of Schema
-- ============================================

