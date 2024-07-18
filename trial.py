import mysql.connector
from mysql.connector import Error

def check_mysql_connection(host, port, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"You're connected to database: {record}")
            cursor.close()
            connection.close()
    except Error as e:
        print(f"Error: {e}")

# Replace with your MySQL server details
check_mysql_connection("localhost",'3305' ,"root", "root", "newschema")
