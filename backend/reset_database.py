"""
Reset Database Script
=====================
Script ini akan:
1. Menghapus semua data dari semua tabel
2. Mereset AUTO_INCREMENT ke 1 untuk semua tabel
3. Menampilkan status reset

PERINGATAN: Script ini akan menghapus SEMUA data di database!
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

def reset_database():
    """Delete all data and reset AUTO_INCREMENT"""
    conn = get_db_connection()
    if not conn:
        print("\n❌ Failed to connect to database!")
        print("Please check your .env file configuration.")
        return False

    try:
        cursor = conn.cursor()
        
        print("\n" + "="*50)
        print("🗑️  RESET DATABASE - Hapus Semua Data")
        print("="*50)
        print("\n⚠️  PERINGATAN: Semua data akan dihapus!")
        print("   Pastikan Anda sudah backup data penting.\n")
        
        # Disable foreign key checks temporarily
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        print("✅ Foreign key checks disabled")
        
        # Delete data in correct order (to avoid foreign key constraint issues)
        tables = [
            'order_items',  # Child table first
            'orders',       # Then parent
            'menu_items',   # Child table
            'restaurants',  # Parent table
            'customers'     # Independent table
        ]
        
        print("\n📋 Menghapus data dari tabel...")
        for table in tables:
            try:
                cursor.execute(f"DELETE FROM {table}")
                deleted_count = cursor.rowcount
                print(f"   ✅ {table}: {deleted_count} rows deleted")
            except Error as e:
                print(f"   ⚠️  {table}: {e}")
        
        # Reset AUTO_INCREMENT for all tables
        print("\n🔄 Mereset AUTO_INCREMENT...")
        auto_increment_tables = [
            'order_items',
            'orders',
            'menu_items',
            'restaurants',
            'customers'
        ]
        
        for table in auto_increment_tables:
            try:
                cursor.execute(f"ALTER TABLE {table} AUTO_INCREMENT = 1")
                print(f"   ✅ {table}: AUTO_INCREMENT reset to 1")
            except Error as e:
                print(f"   ⚠️  {table}: {e}")
        
        # Re-enable foreign key checks
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        print("\n✅ Foreign key checks re-enabled")
        
        # Commit changes
        conn.commit()
        
        print("\n" + "="*50)
        print("✅ DATABASE RESET BERHASIL!")
        print("="*50)
        print("\n📊 Status:")
        print("   • Semua data telah dihapus")
        print("   • AUTO_INCREMENT telah direset ke 1")
        print("   • Database siap untuk data baru")
        print("\n💡 Tips:")
        print("   • Jalankan 'python init_db.py' untuk insert sample data")
        print("   • Atau mulai membuat data baru melalui aplikasi")
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
    print("\n🔧 PastryApp - Database Reset Tool")
    print("="*50)
    
    # Confirmation
    response = input("\n⚠️  Apakah Anda yakin ingin menghapus SEMUA data? (yes/no): ")
    
    if response.lower() in ['yes', 'y', 'ya']:
        success = reset_database()
        if success:
            print("\n✅ Reset selesai!")
        else:
            print("\n❌ Reset gagal!")
    else:
        print("\n❌ Reset dibatalkan.")
        print("   Data tidak dihapus.")

