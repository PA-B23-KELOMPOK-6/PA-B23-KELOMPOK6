import mysql.connector
import pwinput
from invoice import Invoice
from datetime import datetime
from prettytable import PrettyTable

#Connect database
db = mysql.connector.connect(
    host = "Localhost",
    user = "root",
    password = "",
    database = "db_energy_store"
)

cursor = db.cursor()

#Menampilakan tabel produk
def display_produk():
    print(f"{'-'*40:^40}")
    print(f"{'DAFTAR PRODUK':^40}")
    print(f"{'-'*40:^40}")
    try:
        query = "SELECT * FROM produk"
        cursor.execute(query)
        results = cursor.fetchall()

        if cursor.rowcount == 0:
            print("Tidak ada produk yang tersedia.")
            return

        table = PrettyTable()
        table.field_names = ["ID Produk", "Nama Produk", "Merk", "Stok", "Harga Produk", "Biaya Pemasangan"]

        for row in results:
            table.add_row(row)

        print(table)
    except mysql.connector.Error as err:
        print("Error:", err)

#Cek username
def check_username(username):
    query_pembeli = "SELECT COUNT(*) FROM pembeli WHERE username = %s"
    cursor.execute(query_pembeli, (username,))
    result_pembeli = cursor.fetchone()[0]

    query_karyawan = "SELECT COUNT(*) FROM karyawan WHERE username = %s"
    cursor.execute(query_karyawan, (username,))
    result_karyawan = cursor.fetchone()[0]

    if result_pembeli > 0 or result_karyawan > 0:
        return True
    else:
        return False

class Pembeli:
    def beli():
        None
        
    def search():
        print(f"{'-'*40:^40}")
        print(f"{'SEARCH':^40}")
        print(f"{'-'*40:^40}")
        while True:
            search = input("Masukkan nama produk atau merk yang ingin dicari: ")
            try:
                query = "SELECT * FROM produk WHERE nama_produk OR merk LIKE %s"
                cursor.execute(query, (f"%{search}%",))
                results = cursor.fetchall()
                if search.strip():
                    if cursor.rowcount != 0:
                        table = PrettyTable()
                        table.field_names = ["ID Produk", "Nama Produk", "Merk", "Stok", "Harga Produk", "Biaya Pemasangan"]

                        for row in results:
                            table.add_row(row)

                        print(table)
                        break
                    else:
                        print("Produk tidak ditemukan.")
                else:
                    print("Nama produk tidak boleh kosong.")
            except mysql.connector.Error as err:
                print("Error:", err)
    
    def sort_murah():
        print(f"{'-'*40:^40}")
        print(f"{'DAFTAR PRODUK (MURAH - MAHAL)':^40}")
        print(f"{'-'*40:^40}")
        try:
            query = "SELECT * FROM produk ORDER BY `harga_produk` ASC"
            cursor.execute(query)
            results = cursor.fetchall()

            if cursor.rowcount == 0:
                print("Tidak ada produk yang tersedia.")
                return

            table = PrettyTable()
            table.field_names = ["ID Produk", "Nama Produk", "Merk", "Stok", "Harga Produk", "Biaya Pemasangan"]

            for row in results:
                table.add_row(row)

            print(table)
        except mysql.connector.Error as err:
            print("Error:", err)
    
    def sort_mahal():
        print(f"{'-'*40:^40}")
        print(f"{'DAFTAR PRODUK (MAHAL - MURAH)':^40}")
        print(f"{'-'*40:^40}")
        try:
            query = "SELECT * FROM produk ORDER BY `harga_produk` DESC"
            cursor.execute(query)
            results = cursor.fetchall()

            if cursor.rowcount == 0:
                print("Tidak ada produk yang tersedia.")
                return

            table = PrettyTable()
            table.field_names = ["ID Produk", "Nama Produk", "Merk", "Stok", "Harga Produk", "Biaya Pemasangan"]

            for row in results:
                table.add_row(row)

            print(table)
        except mysql.connector.Error as err:
            print("Error:", err)

class NodeProduk:
    def __init__(self, produk):
        self.produk = produk
        self.next = None
#Class karyawan
class LinkedListProduk:
    def __init__(self):
        self.head = None

    def tambah(self, produk):
        node_baru = NodeProduk(produk)
        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node_baru

    def semua(self):
        produk_list = []
        current = self.head
        while current is not None:
            produk_list.append(current.produk)
            current = current.next
        return produk_list

    def cari_by_id(self, id_produk):
        current = self.head
        while current is not None:
            if current.produk["id_produk"] == id_produk:
                return current.produk
            current = current.next
        return None

    def hapus_by_id(self, id_produk):
        if self.head is None:
            return

        if self.head.produk["id_produk"] == id_produk:
            self.head = self.head.next
            return

        previous = None
        current = self.head
        while current is not None and current.produk["id_produk"] != id_produk:
            previous = current
            current = current.next

        if current is not None:
            previous.next = current.next

    def update(self, id_produk, nama=None, merk=None, stok=None, harga=None, biaya_pemasangan=None):
        current = self.head
        while current is not None:
            if current.produk["id_produk"] == id_produk:
                if nama is not None:
                    current.produk["nama_produk"] = nama
                if merk is not None:
                    current.produk["merk"] = merk
                if stok is not None:
                    current.produk["stok"] = stok
                if harga is not None:
                    current.produk["harga_produk"] = harga
                if biaya_pemasangan is not None:
                    current.produk["biaya_pemasangan"] = biaya_pemasangan
                print("Produk berhasil diperbarui.")
                return current.produk
            current = current.next
        print("Produk dengan ID", id_produk, "tidak ditemukan.")
        return None

daftar_produk = LinkedListProduk()

def tambah_produk(nama, merk, stok, harga, biaya_pemasangan):
    query = "INSERT INTO produk (nama_produk, merk, stok, harga_produk, biaya_pemasangan) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nama, merk, stok, harga, biaya_pemasangan))
    db.commit()

    id_baru = cursor.lastrowid
    daftar_produk.tambah({
        "id_produk": id_baru,
        "nama_produk": nama,
        "merk": merk,
        "stok": stok,
        "harga_produk": harga,
        "biaya_pemasangan": biaya_pemasangan
    })
    print("Produk berhasil ditambahkan.")
    
#Login
def login():
    print(f"{'-'*40:^40}")
    print(f"{'MENU LOGIN':^40}")
    print(f"{'-'*40:^40}")
    while True:
        username = input("Username: ")
        password = pwinput.pwinput("Password: ")
        if username and password:
            query = "SELECT * FROM pembeli WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            pembeli = cursor.fetchone()
            if pembeli:
                print("Login berhasil sebagai pembeli.")
                menu_pembeli()
                break
            else:
                query = "SELECT * FROM karyawan WHERE username = %s AND password = %s"
                cursor.execute(query, (username, password))
                karyawan = cursor.fetchone()
                if karyawan:
                    print("Login berhasil sebagai karyawan.")
                    menu_karyawan()
                    break
                else:
                    print("Username atau password salah. Silakan coba lagi.")
        else:
            print("Username dan password harus diisi.")

#Register   
def register():
    while True:
        try:
            print(f"{'-'*40:^40}")
            print(f"{'MENU REGISTRASI':^40}")
            print(f"{'-'*40:^40}")
            nama = input("Masukkan Nama Lengkap: ")
            while True:
                jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")
                if jenis_kelamin.upper() == 'L':
                    jenis_kelamin = 'laki-laki'
                    break
                elif jenis_kelamin.upper() == 'P':
                    jenis_kelamin = 'perempuan'
                    break
                else:
                    print("Masukan tidak valid, Silahkan pilih antara L atau P")
            tanggal_lahir = input("Masukkan tanggal lahir (format: YYYY-MM-DD): ")
            tgl = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
            kota = input("Masukkan kota: ")
            alamat = input("Masukkan alamat rumah: ")
            while True:
                username = input("Masukkan username: ")
                password = pwinput.pwinput("Masukkan password: ")
                if check_username(username):
                    print("Username sudah digunakan. Silakan pilih username lain.\n")
                    continue
                query = "INSERT INTO pembeli (id_pembeli, nama_lengkap, jenis_kelamin, tanggal_lahir, kota, alamat, username, password) VALUES ('', %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (nama, jenis_kelamin, tgl, kota, alamat, username, password))
                db.commit()
                print("Berhasil Register!")
                menu_pembeli()
                break
            break
        except:
            print("Invalid Data")

#Menu Utama
def main_menu():
    while True:
        print(f"{'-'*40:^40}")
        print(f"{'Selamat Datang di Reenergy Store !':^40}")
        print(f"{'-'*40:^40}")
        print("Menu:")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilih = input("Masukkan Pilihan Anda: ")
        if pilih in ['1', '2', '3']:
            if  pilih == '1':
                login()
            elif pilih == '2':
                register()
            elif pilih == '3':
                exit()
        else:
            print("Input salah, silahkan pilih antara 1, 2 dan 3.")
            
#Menu Karyawan
def menu_karyawan():
    while True:
        print(f"\n{'='*100}")
        print(f"{'Menu Kelola Produk':^100}")
        print(f"{'='*100}")
        print("1. Tambah Produk")
        print("2. Lihat Semua Produk")
        print("3. Perbarui Produk")
        print("4. Hapus Produk")
        print("5. Keluar")
        print("="*100)

        try:
            pilihan = int(input("Masukkan pilihan (1-5): "))

            if pilihan == 1:
                nama = input("Masukkan nama produk: ")
                merk = input("Masukkan merk produk: ")
                stok = int(input("Masukkan stok produk: "))
                harga = float(input("Masukkan harga produk: "))
                biaya_pemasangan = float(input("Masukkan biaya pemasangan: "))
                tambah_produk(nama, merk, stok, harga, biaya_pemasangan)

            elif pilihan == 2:
                display_produk()

            elif pilihan == 3:
                id_produk = int(input("Masukkan ID produk yang ingin diperbarui: "))
                nama = input("Nama baru (biarkan kosong jika tidak ingin mengubah): ")
                merk = input("Merk baru (biarkan kosong jika tidak ingin mengubah): ")
                stok = input("Stok baru (biarkan kosong jika tidak ingin mengubah): ")
                harga = input("Harga baru (biarkan kosong jika tidak ingin mengubah): ")
                biaya_pemasangan = input("Biaya pemasangan baru (biarkan kosong jika tidak ingin mengubah): ")

                # Konversi nilai ke float jika diperlukan
                if harga != "":
                    harga = float(harga)
                if biaya_pemasangan != "":
                    biaya_pemasangan = float(biaya_pemasangan)

                # Memperbarui produk
                produk_diperbarui = daftar_produk.update(id_produk, nama, merk, stok, harga, biaya_pemasangan)

                if produk_diperbarui:
                    # Membuat query SQL untuk memperbarui produk di database
                    query = "UPDATE produk (nama_barang, merk, stok, harga_produk, biaya_pemasangan) VALUES (%s, %s, %s, %s, %s) WHERE id_produk = %s"
                    cursor.execute(query, nama, merk, stok, harga, biaya_pemasangan, id_produk)
                    db.commit()
                    print("Produk berhasil diperbarui.")
                else:
                    print("Produk tidak ditemukan.")


            elif pilihan == 4:
                id_produk = int(input("Masukkan ID produk yang ingin dihapus: "))
                daftar_produk.hapus_by_id(id_produk)
                query = "DELETE FROM produk WHERE id_produk = %s"
                cursor.execute(query, (id_produk,))
                db.commit()
                print("Produk berhasil dihapus.")

            elif pilihan == 5:
                print("Keluar dari Menu Kelola Produk.")
                break

            else:
                print("Pilihan tidak valid. Masukkan angka antara 1 dan 5.")

        except ValueError:
            print("Input tidak valid. Masukkan angka.")

#Menu pembeli            
def menu_pembeli():
    print(f"{'-'*40:^40}")
    print(f"{'MENU PEMBELI':^40}")
    print(f"{'-'*40:^40}")
    while True:
        print("1. Beli Produk")
        print("2. Lihat Semua Produk")
        print("3. Urutkan Harga Produk (Murah-Mahal)")
        print("4. Urutkan Harga Produk (Mahal-Murah)")
        print("5. Search Nama Produk")
        print("6. Keluar")

        try:
            pilihan = int(input("Pilih opsi: "))

            if pilihan == 1:
                None
            elif pilihan == 2:
                display_produk()
            elif pilihan == 3:
                Pembeli.sort_murah()
            elif pilihan == 4:
                Pembeli.sort_mahal()
            elif pilihan == 5:
                Pembeli.search()
            elif pilihan == 6:
                break
            else:
                print("Pilihan tidak valid.")

        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

main_menu()