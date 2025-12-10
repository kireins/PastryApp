"""
Reset Orders Only Script
========================
Script ini akan:
1. Menghapus semua data dari tabel orders dan order_items
2. Mereset AUTO_INCREMENT untuk orders dan order_items ke 1
3. TIDAK menghapus data menu, restaurant, atau customers

Berguna untuk reset order history tanpa kehilangan data master.
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

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except Error as e:
        print(f"❌ Error connecting to database: {e}")
        return None

def reset_orders_only():
    """Delete only orders and order_items, reset AUTO_INCREMENT"""
    conn = get_db_connection()
    if not conn:
        print("\n❌ Failed to connect to database!")
        print("Please check your .env file configuration.")
        return False

    try:
        cursor = conn.cursor()
        
        print("\n" + "="*50)
        print("🗑️  RESET ORDERS ONLY - Hapus Data Orders")
        print("="*50)
        print("\n⚠️  PERINGATAN: Semua data orders akan dihapus!")
        print("   ✅ Data menu, restaurant, dan customers TIDAK akan dihapus")
        print("   ✅ Hanya orders dan order_items yang akan dihapus\n")
        
        # Disable foreign key checks temporarily
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        print("✅ Foreign key checks disabled")
        
        # Delete only orders and order_items
        print("\n📋 Menghapus data dari tabel...")
        
        # Delete order_items first (child table)
        try:
            cursor.execute("DELETE FROM order_items")
            deleted_count = cursor.rowcount
            print(f"   ✅ order_items: {deleted_count} rows deleted")
        except Error as e:
            print(f"   ⚠️  order_items: {e}")
        
        # Delete orders (parent table)
        try:
            cursor.execute("DELETE FROM orders")
            deleted_count = cursor.rowcount
            print(f"   ✅ orders: {deleted_count} rows deleted")
        except Error as e:
            print(f"   ⚠️  orders: {e}")
        
        # Reset AUTO_INCREMENT for orders and order_items only
        print("\n🔄 Mereset AUTO_INCREMENT...")
        
        try:
            cursor.execute("ALTER TABLE order_items AUTO_INCREMENT = 1")
            print(f"   ✅ order_items: AUTO_INCREMENT reset to 1")
        except Error as e:
            print(f"   ⚠️  order_items: {e}")
        
        try:
            cursor.execute("ALTER TABLE orders AUTO_INCREMENT = 1")
            print(f"   ✅ orders: AUTO_INCREMENT reset to 1")
        except Error as e:
            print(f"   ⚠️  orders: {e}")
        
        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        print("\n✅ Foreign key checks re-enabled")
        
        # Commit changes
        conn.commit()
        
        print("\n" + "="*50)
        print("✅ ORDERS RESET BERHASIL!")
        print("="*50)
        print("\n📊 Status:")
        print("   • Semua orders dan order_items telah dihapus")
        print("   • AUTO_INCREMENT untuk orders telah direset ke 1")
        print("   • Data menu, restaurant, dan customers TETAP ADA")
        print("   • Database siap untuk order baru")
        print()
        
        cursor.close()
        conn.close()
        return True
        
    except Error as e:
        print(f"\n❌ Error during reset: {e}")
        if conn:
            conn.rollback()
            conn.close()
        return False

if __name__ == '__main__':
    print("\n🔧 PastryApp - Reset Orders Only")
    print("="*50)
    
    # Confirmation
    response = input("\n⚠️  Apakah Anda yakin ingin menghapus SEMUA orders? (yes/no): ")
    
    if response.lower() in ['yes', 'y', 'ya']:
        success = reset_orders_only()
        if success:
            print("\n✅ Reset selesai!")
        else:
            print("\n❌ Reset gagal!")
    else:
        print("\n❌ Reset dibatalkan.")
        print("   Data orders tidak dihapus.")

