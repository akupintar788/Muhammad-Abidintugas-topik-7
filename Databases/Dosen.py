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
sql = "INSERT INTO Dosen (NIP, Nama_Dosen, Matkul, Asal) VALUES (%s, %s, %s, %s)"
val = [
    ('089867555788', 'Sri Handayani', 'OG1', 'Jatirogo' ),
    ('989876456435', 'Siswono', 'OG2', 'sindon'),
    ('088675443343', 'Dwi Atmojo', 'OG3', 'sumbersuko'),
    ('986756478880', 'Indah putri', 'OG4', 'kebonsari'),
    ('232356576887', 'Salsabila hasna putri', 'OG5', 'bogor')
]

cursorObject.executemany(sql, val)

# Commit changes to the database
dataBase.commit()

# Close the cursor and database connection
cursorObject.close()
dataBase.close()