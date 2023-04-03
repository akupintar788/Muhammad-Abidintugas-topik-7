import mysql.connector 

# Connect to MySQL server
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="D3_TI_2023"
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Insert data into Mahasiswa table
sql = "INSERT INTO mahasiswa (NIM, Nama, Alamat, Matkul, Prodi) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('V5565567', 'ody frans wijaya', 'Jl. Ahmad yani. 66', 'OG1', 'THP'),
    ('V8567869', 'muhammad asror alfa', 'Jl. Basuki rahmad. 9', 'OG2', 'AKUN'),
    ('V9786878', 'muhammad farhan ', 'Jl. Sultan thaha syarifuddin No. 3', 'OG3', 'TI'),
    ('V9866785', 'muhammad faldi', 'Jl. Sudirman.no 89', 'OG4', 'FH'),
    ('V9876548', 'muhammad faris', 'Jl. Bung hatta .5', 'OG4', 'FK')
]

cursorObject.executemany(sql, val)

# Commit changes to the database
dataBase.commit()

# Close the cursor and database connection
cursorObject.close()
dataBase.close()