import mysql.connector 

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Create a new database named D3_TI_2023
cursorObject.execute("CREATE DATABASE D3_TI_2023")