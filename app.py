import mysql.connector


def connectionDatabse():
    connector = mysql.connector.connect(
        host="localhost", user="root", password="", database="db_smk"
    )

    if connector.is_connected:
        print("Database Terkoneksi")
        return connector
    else:
        print("Gagal terkoneksi")
        return False


def insertData(nama, nis, jurusan, jenis_kelamin, kelas_id):
    try:
        conn = connectionDatabse()
        cursor = conn.cursor()
        sql = "INSERT INTO Siswa (nama, nis, jurusan, jenis_kelamin, kelas_id) VALUES (%s, %s, %s, %s, %s)"
        data = (nama, nis, jurusan, jenis_kelamin, kelas_id)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil ditambahkan!")

    except mysql.connector.Error as error:
        print("Error : ", error)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def selectAllData():
    try:
        conn = connectionDatabse()
        cursor = conn.cursor()
        sql = "SELECT nama, nis, jurusan, jenis_kelamin, kelas_id FROM Siswa"
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            print(i)

    except mysql.connector.Error as error:
        print("Error : ", error)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def selectOneData(nim):
    try:
        conn = connectionDatabse()
        cursor = conn.cursor()
        sql = "SELECT nama, nis, jurusan, jenis_kelamin, kelas_id FROM Siswa WHERE nim = %s"
        data = (nim,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        if result:
            print(result)
        else:
            print("Data tidak ditemukan!")

    except mysql.connector.Error as error:
        print("Error : ", error)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def updateData(nama, nis, jurusan, jenis_kelamin, kelas_id):
    try:
        conn = connectionDatabse()
        cursor = conn.cursor()
        sql = "UPDATE Siswa SET nama = %s, jenis_kelamin = %s WHERE nim = %s"
        data = (nama, jenis_kelamin, nim)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil diupdate!")

    except mysql.connector.Error as error:
        print("Error : ", error)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def deleteData(nim):
    try:
        conn = connectionDatabse()
        cursor = conn.cursor()
        sql = "DELETE FROM Siswa WHERE nim = %s"
        data = (nim,)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil dihapus!")

    except mysql.connector.Error as error:
        print("Error : ", error)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


while True:
    print("")
    print("========== Menu ==========")
    print("0. Keluar")
    print("1. Tambah Data Siswa")
    print("2. Tampilkan Seluruh Data Siswa")
    print("3. Tampilkan Data Siswa berdasarkan NIM")
    print("4. Edit Data Siswa")
    print("5. Delete Data Siswa")
    inputMenu = input("Pilih menu [0-5] : ")
    if inputMenu == "0":
        break
    elif inputMenu == "1":
        print("")
        nim = input("Masukkan NIM : ")
        nama = input("Masukkan Nama : ")
        print("Jenis Kelamin : ")
        print("1. Laki-laki")
        print("2. Perempuan")
        jenis_kelamin = input("Pilih jenis kelamin [1-2] : ")
        if jenis_kelamin == "1":
            jenis_kelamin = "Laki-laki"
        elif jenis_kelamin == "2":
            jenis_kelamin = "Perempuan"
        insertData(nama, nis, jurusan, jenis_kelamin, kelas_id)
    elif inputMenu == "2":
        print("")
        selectAllData()
    elif inputMenu == "3":
        print("")
        nim = input("Masukkan NIM : ")
        selectOneData(nim)
    elif inputMenu == "4":
        print("")
        nim = input("Masukkan NIM yang akan diupdate : ")
        nama = input("Masukkan nama baru : ")
        print("Jenis Kelamin : ")
        print("1. Laki-laki")
        print("2. Perempuan")
        jenis_kelamin = input("Pilih jenis kelamin [1-2] : ")
        if jenis_kelamin == "1":
            jenis_kelamin = "Laki-laki"
        elif jenis_kelamin == "2":
            jenis_kelamin = "Perempuan"
        updateData(nama, nis, jurusan, jenis_kelamin, kelas_id)
    elif inputMenu == "5":
        print("")
        nim = input("Masukkan NIM yang akan dihapus : ")
        deleteData(nim)
