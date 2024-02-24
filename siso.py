import mysql.connector

# Replace 'afsar' with the correct password
db_connection = mysql.connector.connect(
    host='localhost',
    user='ODBC',
    password='afsar',
    database='RPMnew_dataBase'
)

# Close the connection
db_connection.close()
print(db_connection)
