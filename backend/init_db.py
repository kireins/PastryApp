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

def create_database_and_tables():
    """Create database and tables"""
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Create database
        database_name = os.getenv('MYSQL_DATABASE', 'pastry_db')
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created or already exists.")

        # Select database
        cursor.execute(f"USE {database_name}")

        # Create customers table
        create_customers_table = """
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            phone VARCHAR(20) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_customers_table)
        print("Customers table created or already exists.")

        # Create restaurants table
        create_restaurants_table = """
        CREATE TABLE IF NOT EXISTS restaurants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_restaurants_table)
        print("Restaurants table created or already exists.")

        # Create menu_items table
        create_menu_items_table = """
        CREATE TABLE IF NOT EXISTS menu_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            restaurant_id INT NOT NULL,
            name VARCHAR(255) NOT NULL,
            price INT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id) ON DELETE CASCADE
        )
        """
        cursor.execute(create_menu_items_table)
        print("Menu items table created or already exists.")

        # Create orders table
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
            FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
        )
        """
        cursor.execute(create_orders_table)
        print("Orders table created or already exists.")

        # Create order_items table
        create_order_items_table = """
        CREATE TABLE IF NOT EXISTS order_items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            order_id INT NOT NULL,
            menu_id INT NOT NULL,
            quantity INT NOT NULL,
            price INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
            FOREIGN KEY (menu_id) REFERENCES menu_items(id) ON DELETE CASCADE
        )
        """
        cursor.execute(create_order_items_table)
        print("Order items table created or already exists.")

        conn.commit()
        print("\n✅ All tables created successfully!")

        # Insert sample data
        insert_sample_data(cursor, conn, database_name)

        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error: {e}")

def insert_sample_data(cursor, conn, database_name):
    """Insert sample data into tables"""
    try:
        # Check if sample data already exists
        cursor.execute("SELECT COUNT(*) FROM customers")
        if cursor.fetchone()[0] > 0:
            print("\n⏭️  Sample data already exists. Skipping insertion.")
            return

        # Insert customers
        customers_data = [
            ('John Doe', 'john@example.com', '081234567890'),
            ('Jane Smith', 'jane@example.com', '082345678901')
        ]
        cursor.executemany(
            "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)",
            customers_data
        )
        print("✅ Sample customers inserted.")

        # Insert restaurant
        cursor.execute(
            "INSERT INTO restaurants (name, location) VALUES (%s, %s)",
            ('Pastry', 'Jakarta, Indonesia')
        )
        print("✅ Sample restaurant inserted.")

        # Insert menu items
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
        print("\n✅ Sample data inserted successfully!")

    except Error as e:
        print(f"Error inserting sample data: {e}")

if __name__ == '__main__':
    print("🔧 Creating database and tables...\n")
    create_database_and_tables()
