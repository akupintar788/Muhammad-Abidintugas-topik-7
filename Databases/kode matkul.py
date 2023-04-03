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
sql = "INSERT INTO mataKuliah (Kode_Matkul, Nama_Matkul, Waktu, Ruangan, Prodi) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('OG1', 'Matematika informatika', '1999-08-02', 'R1L1', 'THP'),
    ('OG2', 'praktik APSI', '1999-08-03', 'R1L2', 'AKUN'),
    ('OG3', 'Agama', '1999-08-04', 'R1L3', 'TI'),
    ('OG4', 'PPKN', '1999-08-05', 'R2L1', 'FH'),
    ('OG5', 'MTK', '1999-08-06', 'R2L2', 'FK')
]

cursorObject.executemany(sql, val)

# Commit changes to the database
dataBase.commit()

# Close the cursor and database connection
cursorObject.close()
dataBase.close()