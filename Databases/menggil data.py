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

# Execute the SELECT query
sql = "SELECT Mahasiswa.NIM, Mahasiswa.Nama, MataKuliah.Nama_Matkul, Dosen.Nama_Dosen        FROM Mahasiswa        JOIN MataKuliah ON Mahasiswa.Matkul = MataKuliah.Kode_Matkul        JOIN Dosen ON MataKuliah.Kode_Matkul = Dosen.Matkul"

cursorObject.execute(sql)

# Fetch all the rows
result = cursorObject.fetchall()

# Print the result
for row in result:
    print("---------------------------")
    print("NIM             : ", row[0])
    print("NAMA            : ", row[1])
    print("MataKuliah      : ", row[2])
    print("Dosen Pengajar  : ", row[3])
    print("---------------------------")

# Close the cursor and database connection
cursorObject.close()
dataBase.close()