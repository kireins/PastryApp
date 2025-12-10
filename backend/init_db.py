import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

# MySQL Configuration
db_config = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'port': int(os.getenv('MYSQL_PORT', 3306))
}

def create_customer_database():
    """Create customer database and tables"""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS customer_db")
        print("✅ Database 'customer_db' created or already exists.")
        
        cursor.execute("USE customer_db")
        
        # Create customers table
        create_customers_table = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
        cursor.execute(create_customers_table)
        print("✅ Customers table created or already exists.")
        
        # Insert sample data
        cursor.execute("SELECT COUNT(*) FROM customers")
        if cursor.fetchone()[0] == 0:
            customers_data = [
                ('John Doe', 'john@example.com', '081234567890'),
                ('Jane Smith', 'jane@example.com', '082345678901')
            ]
            cursor.executemany(
                "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)",
                customers_data
            )
            print("✅ Sample customers inserted.")
        
        conn.commit()
        cursor.close()
        conn.close()
        
    except Error as e:
        print(f"❌ Error creating customer database: {e}")

def create_restaurant_database():
    """Create restaurant database and tables"""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS restaurant_db")
        print("✅ Database 'restaurant_db' created or already exists.")
        
        cursor.execute("USE restaurant_db")
        
        # Create restaurants table
        create_restaurants_table = """
        CREATE TABLE IF NOT EXISTS restaurants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
        cursor.execute(create_restaurants_table)
        print("✅ Restaurants table created or already exists.")
        
        # Insert sample data
        cursor.execute("SELECT COUNT(*) FROM restaurants")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO restaurants (name, location) VALUES (%s, %s)",
                ('Pastry', 'Jakarta, Indonesia')
            )
            print("✅ Sample restaurant inserted.")
        
        conn.commit()
        cursor.close()
        conn.close()
        
    except Error as e:
        print(f"❌ Error creating restaurant database: {e}")

def create_menu_database():
    """Create menu database and tables"""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS menu_db")
        print("✅ Database 'menu_db' created or already exists.")
        
        cursor.execute("USE menu_db")
        
        # Create menu_items table (no FK constraint for database-per-service pattern)
        create_menu_items_table = """
        CREATE TABLE IF NOT EXISTS menu_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            restaurant_id INT NOT NULL,
            name VARCHAR(255) NOT NULL,
            price INT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_restaurant_id (restaurant_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
        cursor.execute(create_menu_items_table)
        print("✅ Menu items table created or already exists.")
        
        # Insert sample data
        cursor.execute("SELECT COUNT(*) FROM menu_items")
        if cursor.fetchone()[0] == 0:
            menu_items_data = [
                (1, 'Chocolate Croissant', 35000, 'Delicious chocolate filled croissant'),
                (1, 'Strawberry Tart', 45000, 'Fresh strawberry tart with cream'),
                (1, 'Vanilla Donut', 25000, 'Soft vanilla donut with glaze'),
                (1, 'Matcha Cake', 55000, 'Premium matcha cake')
            ]
            cursor.executemany(
                "INSERT INTO menu_items (restaurant_id, name, price, description) VALUES (%s, %s, %s, %s)",
                menu_items_data
            )
            print("✅ Sample menu items inserted.")
        
        conn.commit()
        cursor.close()
        conn.close()
        
    except Error as e:
        print(f"❌ Error creating menu database: {e}")

def create_order_database():
    """Create order database and tables"""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS order_db")
        print("✅ Database 'order_db' created or already exists.")
        
        cursor.execute("USE order_db")
        
        # Create orders table (no FK to customers for database-per-service pattern)
        create_orders_table = """
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
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
        cursor.execute(create_orders_table)
        print("✅ Orders table created or already exists.")
        
        # Create order_items table (no FK to menu_items for database-per-service pattern)
        create_order_items_table = """
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
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
        cursor.execute(create_order_items_table)
        print("✅ Order items table created or already exists.")
        
        conn.commit()
        cursor.close()
        conn.close()
        
    except Error as e:
        print(f"❌ Error creating order database: {e}")

def create_all_databases():
    """Create all databases for microservices"""
    print("🔧 Creating databases for microservices (Database-Per-Service pattern)...\n")
    
    create_customer_database()
    print()
    create_restaurant_database()
    print()
    create_menu_database()
    print()
    create_order_database()
    print()
    
    print("✅ All databases created successfully!")
    print("\n📊 Database Summary:")
    print("   - customer_db: Customer Service")
    print("   - restaurant_db: Restaurant Service")
    print("   - menu_db: Menu Service")
    print("   - order_db: Order Service")

if __name__ == '__main__':
    create_all_databases()
