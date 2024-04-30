### Dokumentasi

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

# Flowchart
![WhatsApp Image 2024-04-30 at 18 17 15](https://github.com/PA-B23-KELOMPOK-6/PA-B23-KELOMPOK6/assets/109202315/8b940ef7-1081-4ac6-a74a-71616f0cf83b)

![WhatsApp Image 2024-04-30 at 18 17 15 (1)](https://github.com/PA-B23-KELOMPOK-6/PA-B23-KELOMPOK6/assets/109202315/e807db88-b020-4fdd-abf0-02e8cc4a9b14)

![WhatsApp Image 2024-04-30 at 18 17 16](https://github.com/PA-B23-KELOMPOK-6/PA-B23-KELOMPOK6/assets/109202315/15fbf6a6-0645-4e73-bf74-44440650fa53)

![WhatsApp Image 2024-04-30 at 18 17 16 (1)](https://github.com/PA-B23-KELOMPOK-6/PA-B23-KELOMPOK6/assets/109202315/7619d1e9-a231-4298-a927-2b8d8e2bbd11)


# Class Karyawan
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

    def tambah_produk():
        while True:
            nama = input("Masukkan nama produk: ")
            merk = input("Masukkan merk produk: ")
            stok = int(input("Masukkan stok produk: "))
            harga = float(input("Masukkan harga produk: "))
            biaya_pemasangan = float(input("Masukkan biaya pemasangan: "))
            if nama.strip() and merk.strip():
                query = "INSERT INTO produk (nama_produk, merk, stok, harga_produk, biaya_pemasangan) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(
                    query, (nama, merk, stok, harga, biaya_pemasangan))
                db.commit()
                break
            else:
                print("Nama dan Merk Tidak Boleh Kosong!")

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

    def delete_related_transaksi(id_produk):
        try:
            query = "DELETE FROM transaksi WHERE id_produk = %s"
            cursor.execute(query, (id_produk,))
            db.commit()
        except mysql.connector.Error as err:
            db.rollback()

    def hapus_produk(id_produk):
        try:
            query = "SELECT * FROM produk WHERE id_produk = %s"
            cursor.execute(query, (id_produk,))
            produk = cursor.fetchone()

            if produk:
                LinkedListProduk.delete_related_transaksi(id_produk)
                query = "DELETE FROM produk WHERE id_produk = %s"
                cursor.execute(query, (id_produk,))
                db.commit()
                print("Produk berhasil dihapus.")
            else:
                print(f"Produk dengan ID {id_produk} tidak ditemukan.")

        except ValueError:
            print("ID produk harus berupa bilangan bulat.")

        except mysql.connector.Error as err:
            db.rollback()
            print("Error saat menghapus produk:", err)

    def update(id_produk):
        nama = input("Masukkan nama produk baru (opsional): ")
        merk = input("Masukkan merk baru (opsional): ")
        stok = input("Masukkan jumlah stok baru (opsional): ")
        harga = input("Masukkan harga baru (opsional): ")
        biaya_pemasangan = input("Biaya pemasangan baru (opsional): ")

        if nama.strip() == "":
            nama = None
        if merk.strip() == "":
            merk = None
        if stok.strip() == "":
            stok = None
        else:
            stok = int(stok)
        if harga.strip() == "":
            harga = None
        else:
            harga = float(harga)
        if biaya_pemasangan.strip() == "":
            biaya_pemasangan = None
        else:
            biaya_pemasangan = float(biaya_pemasangan)

        # Update hanya dilakukan jika ada input yang diisi
        if nama or merk or stok or harga or biaya_pemasangan:
            query = "UPDATE produk SET nama_produk = COALESCE(%s, nama_produk), merk = COALESCE(%s, merk), stok = COALESCE(%s, stok), harga_produk = COALESCE(%s, harga_produk), biaya_pemasangan = COALESCE(%s, biaya_pemasangan) WHERE id_produk = %s"
            values = (nama, merk, stok, harga, biaya_pemasangan, id_produk)
            cursor.execute(query, values)
            db.commit()
            print("Produk berhasil diperbarui.")
        else:
            print("Tidak ada perubahan yang dilakukan.")


daftar_produk = LinkedListProduk()

## Penjelasan
  - Program di atas ini adalah class untuk karyawan, ini mencakup fungsi karyawan dan linked list, yaitu sperti menambahkan produk, mengedit produk, lihat produk, dan hapus produk.


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
