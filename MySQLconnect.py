import mysql.connector

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',        # default user in XAMPP
        password='',         # leave empty if no password
        database='mmust.db'    # replace with your database name
    )

    if connection.is_connected():
        print("✅ Connected to MySQL database")
    else:
        print("❌ Failed to connect to MySQL database")
except Error as e:
    print(f"❌ Error while connecting to MySQL: {e}")
        
    

        
