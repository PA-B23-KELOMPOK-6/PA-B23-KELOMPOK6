# PA-B23-KELOMPOK6
### Deskripsi Program
# Tujuan Program

  -Dapat Menyediakan Penjualanan yang dapat diakses dengan mudah dan dapat dijangkau di desa maupun di kota.

  -Reenergy Store berusaha untuk mengatasi tantangan logistik dan aksesibilitas yang menjadi hambatan utama dalam pengiriman dan pemasangan peralatan energi terbarukan di daerah terpencil.

  -Melalui langkah-langkah yang diambil di Kutai Barat, Reenergy Store juga memiliki tujuan untuk memberikan inspirasi dan mendorong pengembangan energi terbarukan di daerah terpencil lainnya

  # Manfaat

    -Penduduk di daerah terpencil kini memiliki akses ke listrik yang lebih stabil dan berkelanjutan, yang mendukung aktivitas sehari-hari dan meningkatkan kualitas hidup.

    -Dengan mengandalkan sumber daya alam energi terbarukan seperti matahari, Reenergy Store membantu mengurangi dampak lingkungan dan jejak karbon.

    -Dengan melibatkan tenaga kerja lokal dalam pemasangan dan pemeliharaan, perusahaan ini membantu meningkatkan keterampilan dan membuka peluang kerja bagi penduduk setempat.

    -Dengan adanya akses listrik yang baik hal itu akan membatu perkembangan ekonomi di daerah tersebut dan dapat memberikan peluang bagi usaha kecil untuk meningkatkan produktivitas komunitas.

# Penjelasan struktur project

Program:
# db_connection.py
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        db = mysql.connector.connect(
            host="sql6.freesqldatabase.com",
            user="sql6702194",
            password="t6ayvq7vPm",
            database="sql6702194"
        )
        if db.is_connected():
            return db
    except Error as e:
        print("Error connecting to MySQL", e)
    return None

## Penjelasan
  -Jadi program diatas sebagai Database Connection ini bertanggung jawab untuk menghubungkan ke database MySQL. Modul ini dapat dinamakan db_connection.py dan berisi kode untuk koneksi serta penanganan kesalahan.


program:
# data_structures.py
class NodeProduk:
    def __init__(self, produk):
        self.produk = produk
        self.next = None


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

    def cari(self, id_produk):
        current = self.head
        while current:
            if current.produk["id_produk"] == id_produk:
                return current.produk
            current = current.next
        return None

    def hapus(self, id_produk):
        current = self.head
        prev = None
        while current:
            if current.produk["id_produk"] == id_produk:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

## Penjelasan
  - Program di atas ini adalah Data Structures,ini mencakup definisi struktur data untuk produk dan linked list, serta operasi dasar seperti penambahan, penghapusan, dan pencarian. Modul ini dapat dinamakan data_structures.py.


program:
# display.py
def display_produk(cursor):
    try:
        query = "SELECT * FROM produk"
        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("Tidak ada produk yang tersedia.")
            return

        table = PrettyTable()
        table.field_names = ["ID Produk", "Nama Produk", "Merk", "Stok", "Harga Produk", "Biaya Pemasangan"]

        for row in results:
            if row[3] == 0:
                row = list(row)
                row[3] = "Stok Habis"
            table.add_row(row)

        print(table)
    except mysql.connector.Error as err:
        print("Error:", err)

## Penjelasan
  -Program diatas ini adalah Display, ini berisi fungsi untuk menampilkan data dalam bentuk tabel. Biasanya, modul ini menggunakan PrettyTable untuk menampilkan tabel yang rapi dan mudah dibaca. Modul ini dapat dinamakan display.py.


Program:
# main.py
import db_connection

import display

import data_structures

import pwinput

from datetime import datetime

db = db_connection.create_connection()
if db:
    cursor = db.cursor()

    # Logika utama program
def main_menu():
    print("Selamat Datang di Reenergy Store!")
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            login()
        elif pilihan == '2':
            register()
        elif pilihan == '3':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

            # Definisi login dan register
def login():
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")
    if username and password:
        # Cek di database pembeli dan karyawan
        # (Implementasikan logika login)

def register():
    # Logika registrasi pembeli baru
    # (Implementasikan logika registrasi)

main_menu()  # Memulai program

## Penjelasan:
  -Program di atas adalah Main Program, ini berisi logika utama dari program, termasuk antarmuka pengguna, pemrosesan input, dan penggunaan modul-modul sebelumnya. Modul ini dapat dinamakan main.py.


  Program:

  models/
├── admin.py

├── perkotaan.py

├── pemukiman.py

├── proyek.py

## Penjelasan:
  -Models Directory Direktori ini berisi model-model data yang digunakan dalam program. Sebagai contoh, modul untuk data admin (admin.py), data perkotaan (perkotaan.py), data pemukiman (pemukiman.py), dan data proyek (proyek.py). Setiap file dalam direktori models berisi definisi model data serta operasi yang berkaitan dengan model tersebut.


Program:
admin/

├── admin.py

├── admin_utils.py


## Penjelasan:
-Admin Directory
Direktori ini mengelola operasi-admin, seperti pengelolaan data admin. Bisa juga menyertakan utilitas yang dapat digunakan dalam modul admin. File admin.py berisi fungsi-fungsi yang terkait dengan admin, sedangkan admin_utils.py berisi utilitas untuk membantu operasi admin.

## Fitur

## Login & Registrasi:
-Login = User dapat login dengan memasukkan username dan password. Jika login berhasil, user akan diarahkan ke menu sesuai dengan perannya, baik sebagai pembeli maupun karyawan.

-Registrasi = User yang belum memiliki akun dapat membuat akun baru dengan mengisi informasi pribadi, seperti nama lengkap, jenis kelamin, tanggal lahir, kota, alamat, username, dan password.

-Keluar = Jika user memilih opsi keluar, program akan berhenti dan keluar.

## Manajemen Produk:
-Lihat Semua Produk = Menampilkan daftar produk yang tersedia dalam bentuk tabel. Setiap produk memiliki detail seperti ID produk, nama, merk, stok, harga, dan biaya pemasangan. Stok yang habis ditandai dengan teks "Stok Habis".

-Tambah Produk = Karyawan atau admin dapat menambahkan produk baru dengan memasukkan detail seperti nama produk, merk, stok, harga, dan biaya pemasangan.

-Perbarui Produk = Karyawan atau admin dapat memperbarui informasi produk yang sudah ada, seperti nama produk, merk, stok, harga, atau biaya pemasangan.

-Hapus Produk = Karyawan atau admin dapat menghapus produk dari database dengan memasukkan ID produk yang ingin dihapus.

## Transaksi & Pembelian:
-Beli Produk = Fitur ini memungkinkan pembeli untuk membeli produk dari toko dengan memasukkan ID produk dan jumlah yang ingin dibeli. Jika stok mencukupi, pembeli dapat melanjutkan transaksi.

-Tampilkan Invoice = Setelah pembelian berhasil, pembeli dapat melihat invoice yang menampilkan detail pembelian, termasuk produk yang dibeli, jumlah, harga, biaya pemasangan, dan total harga.

-Simpan Transaksi = Setelah pembayaran dikonfirmasi, sistem akan mengurangi stok produk sesuai dengan jumlah yang dibeli dan mencatat transaksi ke dalam database.

## Sorting & Pencarian:
-urutkan Produk (Murah - Mahal) = Fitur ini mengurutkan daftar produk berdasarkan harga, dari yang termurah hingga termahal.

-Urutkan Produk (Mahal - Murah) = Fitur ini mengurutkan daftar produk berdasarkan harga, dari yang termahal hingga termurah.

-Cari Produk = Pembeli dapat mencari produk berdasarkan nama atau merk. Sistem akan menampilkan produk yang sesuai dengan kata kunci pencarian.

## Koneksi Database:
-Database Configuration = Menyediakan konfigurasi untuk menghubungkan ke database MySQL. Konfigurasi ini mencakup parameter seperti host, user, password, dan nama database.

-Cursor = Objek yang digunakan untuk mengeksekusi query SQL dan mengambil hasil dari database. Cursor memungkinkan program berinteraksi dengan data yang tersimpan dalam database.

## Lingked list & class:
-Kelas Pembeli = Kelas yang menangani operasi terkait pembeli, seperti pembelian produk, menampilkan invoice, dan menyimpan transaksi. Kelas ini mempunyai metode untuk melakukan pembelian, menyimpan transaksi, dan menampilkan invoice.

-LinkedListProduk = Struktur data yang digunakan untuk mengelola produk dalam bentuk linked list. Struktur ini memungkinkan penambahan, penghapusan, dan pembaruan produk dalam daftar.

## Penanganan eror:
-Error Handling = Fitur ini menangani kesalahan yang mungkin terjadi selama operasi database. Menggunakan kelas mysql.connector.Error untuk menangani kesalahan saat menjalankan query SQL atau saat koneksi database mengalami masalah.
