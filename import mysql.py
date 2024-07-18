# import mysql.connector

# # MySQL connection parameters
# config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'root',
#     'database': 'newschema'
# }

# try:
#     # Connect to MySQL
#     conn = mysql.connector.connect(**config)

#     if conn.is_connected():
#         print('Connected to MySQL database')

#         # Perform operations
#         # For example, execute a query
#         cursor = conn.cursor()
#         cursor.execute('SELECT * FROM schedule')
#         rows = cursor.fetchall()
        
#         for row in rows:
#             print(row)

# except mysql.connector.Error as e:
#     print(f'Error connecting to MySQL: {e}')

# finally:
#     # Close connection
#     if 'conn' in locals() and conn.is_connected():
#         cursor.close()
#         conn.close()
#         print('MySQL connection closed')

import mysql.connector

try:
    # MySQL connection parameters
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'Balpande@23',
        'database': 'newschema',
        'port': '3306'
    }

    # Connect to MySQL
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print('Connected to MySQL database')

        # Perform operations
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM schedule')
        rows = cursor.fetchall()
        
        for row in rows:
            print(row)

except mysql.connector.Error as e:
    print(f'Error connecting to MySQL: {e}')

finally:
    # Close connection
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print('MySQL connection closed')
