import mysql.connector
import random


def connectionDatabse():
    connector = mysql.connector.connect(
        host="localhost", user="root", password="", database="db_smk"
    )

    if connector.is_connected:
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
        sql = "SELECT siswa.nama, siswa.nis, siswa.jurusan, siswa.jenis_kelamin, kelas.nama_kelas, kelas.wali_kelas FROM siswa INNER JOIN kelas ON siswa.kelas_id = kelas.id"
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


def selectOneData(nis):
    try:
        conn = connectionDatabse()
        cursor = conn.cursor()
        sql = "SELECT siswa.nama, siswa.nis, siswa.jurusan, siswa.jenis_kelamin, kelas.nama_kelas, kelas.wali_kelas FROM siswa INNER JOIN kelas ON siswa.kelas_id = kelas.id WHERE nis = %s"
        data = (nis,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        if result:
            print("Nama :", result[0][0])
            print("NIS :", result[0][1])
            print("Jurusan :", result[0][2])
            print("Jenis Kelamin :", result[0][3])
            print("Kelas :", result[0][4])
            print("Wali Kelas :", result[0][5])
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
        sql = "UPDATE Siswa SET nama = %s, jurusan = %s, jenis_kelamin = %s, kelas_id = %s WHERE nis = %s"
        data = (nama, jurusan, jenis_kelamin, kelas_id, nis)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil diupdate!")

    except mysql.connector.Error as error:
        print("Error : ", error)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def deleteData(nis):
    try:
        conn = connectionDatabse()
        cursor = conn.cursor()
        sql = "DELETE FROM siswa WHERE nis = %s"
        data = (nis,)
        cursor.execute(sql, data)
        conn.commit()
        print("Data berhasil dihapus!")

    except mysql.connector.Error as error:
        print("Error : ", error)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def selectClass(kelas_id):
    try:
        conn = connectionDatabse()
        cursor = conn.cursor()
        sql = "SELECT siswa.nama, siswa.nis, siswa.jurusan, siswa.jenis_kelamin, kelas.nama_kelas, kelas.wali_kelas FROM siswa INNER JOIN kelas ON siswa.kelas_id = kelas.id WHERE kelas_id = %s"
        data = (kelas_id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        for i in result:
            print(i)

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
    print("3. Tampilkan Data Siswa berdasarkan NIS")
    print("4. Edit Data Siswa")
    print("5. Delete Data Siswa")
    print("6. Tampilkan Anggota Kelas")
    inputMenu = input("Pilih menu [0-6] : ")
    if inputMenu == "0":
        break
    elif inputMenu == "1":
        print("")
        nama = input("Masukkan Nama : ")
        nis = input("Masukkan NIS : ")
        print("Jurusan : ")
        print("1. Rekayasa Perangkat Lunak")
        print("2. Teknik Komputer dan Jaringan")
        print("3. Desain Komunikasi Visual")
        jurusan = input("Pilih jurusan [1-3] : ")
        if jurusan == "1":
            jurusan = "Rekayasa Perangkat Lunak"
            kelas_id = random.randint(1, 2)
        elif jurusan == "2":
            jurusan = "Teknik Komputer dan Jaringan"
            kelas_id = random.randint(3, 4)
        elif jurusan == "3":
            jurusan = "Desain Komunikasi Visual"
            kelas_id = random.randint(5, 6)
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
        nis = input("Masukkan NIS : ")
        print("")
        selectOneData(nis)
    elif inputMenu == "4":
        print("")
        nis = input("Masukkan NIS yang akan diupdate : ")
        nama = input("Masukkan nama baru : ")
        print("Jurusan : ")
        print("1. Rekayasa Perangkat Lunak")
        print("2. Teknik Komputer dan Jaringan")
        print("3. Desain Komunikasi Visual")
        jurusan = input("Pilih jurusan [1-3] : ")
        if jurusan == "1":
            jurusan = "Rekayasa Perangkat Lunak"
            kelas_id = random.randint(1, 2)
        elif jurusan == "2":
            jurusan = "Teknik Komputer dan Jaringan"
            kelas_id = random.randint(3, 4)
        elif jurusan == "3":
            jurusan = "Desain Komunikasi Visual"
            kelas_id = random.randint(5, 6)
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
        nis = input("Masukkan NIS yang akan dihapus : ")
        deleteData(nis)
    elif inputMenu == "6":
        print("")
        print("Kelas : ")
        print("=== Rekayasa Perangkat Lunak ===")
        print("1. A")
        print("2. B")
        print("=== Teknik Komputer dan Jaringan ===")
        print("3. C")
        print("4. D")
        print("=== Desain Komunikasi Visual ===")
        print("5. E")
        print("6. F")
        kelas_id = int(input("Pilih kelas [1-6] : "))
        print("")
        print("Anggota Kelas :")
        selectClass(kelas_id)
