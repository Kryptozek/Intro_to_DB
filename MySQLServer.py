# MySQLServer.py

import mysql.connector
from mysql.connector import Error  # Import the MySQL-specific Error class

def create_database():
    try:
        # Establish connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',  # Replace with your MySQL host if different
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Creating the database alx_book_store
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Correct MySQL error handling
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
