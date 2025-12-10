"""
Migration script to change price columns from DECIMAL(10,2) to INT
Run this script if you have existing data in the database.
"""
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
    'database': os.getenv('MYSQL_DATABASE', 'pastry_db'),
    'port': int(os.getenv('MYSQL_PORT', 3306))
}

def migrate_price_columns():
    """Migrate price columns from DECIMAL to INT"""
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        print("Starting migration: DECIMAL(10,2) to INT\n")
        
        # Migrate menu_items.price
        try:
            print("1. Migrating menu_items.price...")
            cursor.execute("ALTER TABLE menu_items MODIFY COLUMN price INT NOT NULL")
            print("   [OK] menu_items.price migrated successfully")
        except Error as e:
            print(f"   [WARNING] menu_items.price: {e}")
        
        # Migrate orders.total_price
        try:
            print("2. Migrating orders.total_price...")
            cursor.execute("ALTER TABLE orders MODIFY COLUMN total_price INT NOT NULL")
            print("   [OK] orders.total_price migrated successfully")
        except Error as e:
            print(f"   [WARNING] orders.total_price: {e}")
        
        # Migrate orders.tax
        try:
            print("3. Migrating orders.tax...")
            cursor.execute("ALTER TABLE orders MODIFY COLUMN tax INT NOT NULL")
            print("   [OK] orders.tax migrated successfully")
        except Error as e:
            print(f"   [WARNING] orders.tax: {e}")
        
        # Migrate order_items.price
        try:
            print("4. Migrating order_items.price...")
            cursor.execute("ALTER TABLE order_items MODIFY COLUMN price INT NOT NULL")
            print("   [OK] order_items.price migrated successfully")
        except Error as e:
            print(f"   [WARNING] order_items.price: {e}")
        
        conn.commit()
        print("\n[SUCCESS] Migration completed successfully!")
        
        cursor.close()
        conn.close()
        
    except Error as e:
        print(f"[ERROR] Error during migration: {e}")
        print("\n[WARNING] If you get errors, you may need to:")
        print("   1. Drop and recreate the database (will lose all data)")
        print("   2. Or manually convert DECIMAL values to INT in the database")

if __name__ == '__main__':
    import sys
    
    print("=" * 50)
    print("PRICE COLUMN MIGRATION: DECIMAL to INT")
    print("=" * 50)
    print("\n[WARNING] This will convert all price values to integers.")
    print("   Decimal values will be rounded to nearest integer.\n")
    
    # Check if --yes flag is provided for non-interactive mode
    if '--yes' in sys.argv or '-y' in sys.argv:
        migrate_price_columns()
    else:
        try:
            response = input("Do you want to continue? (yes/no): ")
            if response.lower() == 'yes':
                migrate_price_columns()
            else:
                print("Migration cancelled.")
        except EOFError:
            # Non-interactive mode, auto-confirm
            print("[INFO] Running in non-interactive mode. Proceeding with migration...")
            migrate_price_columns()

