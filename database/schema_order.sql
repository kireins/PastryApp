-- ============================================
-- Order Service Database Schema
-- ============================================
-- Database: order_db
-- Created: 2025
-- ============================================

-- Create Database
CREATE DATABASE IF NOT EXISTS order_db;
USE order_db;

-- ============================================
-- Table: orders
-- Description: Stores order information
-- Note: customer_id is stored but FK constraint removed for database-per-service pattern
-- ============================================
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    customer_username VARCHAR(255) NOT NULL,
    customer_name VARCHAR(255) NOT NULL,
    customer_email VARCHAR(255) NOT NULL,
    customer_phone VARCHAR(20) NOT NULL,
    delivery_address VARCHAR(255) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    total_price INT NOT NULL,
    tax INT NOT NULL,
    status ENUM('on_process', 'on_delivery', 'delivered') DEFAULT 'on_process',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_customer_id (customer_id),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- Table: order_items
-- Description: Stores items in each order
-- Note: menu_id is stored but FK constraint removed for database-per-service pattern
-- ============================================
CREATE TABLE IF NOT EXISTS order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    menu_id INT NOT NULL,
    quantity INT NOT NULL,
    price INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    INDEX idx_order_id (order_id),
    INDEX idx_menu_id (menu_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================
-- End of Schema
-- ============================================

