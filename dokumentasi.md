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


# class Karyawan
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
Class Karyawan berfungsi untuk mencakup fungsi karyawan dan linked list, yaitu sperti menambahkan produk, mengedit produk, lihat produk, dan hapus produk.

# def display_produk
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
            if row[3] == 0:
                row = list(row)
                row[3] = "Stok Habis"
            table.add_row(row) 
            
        print(table)
    except mysql.connector.Error as err:
        print("Error:", err)

## Penjelasan
Program diatas ini adalah Display, ini berisi fungsi untuk menampilkan data dalam bentuk tabel. Modul ini menggunakan PrettyTable untuk menampilkan tabel yang rapi dan mudah dibaca.

# def check_username
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

## Penjelasan
Program di atas berfungsi untuk mengecek apakah yang username saat register sudah ada pada database atau belum.

# class Pembeli

    class Pembeli:
        def __init__(self, cursor, db):
            self.cursor = cursor
            self.db = db
            self.invoice = []

    def simpan_transaksi(self):
        try:
            for item in self.invoice:
                query = "UPDATE produk SET stok = stok - %s WHERE id_produk = %s"
                self.cursor.execute(query, (item["jumlah"], item["id_produk"]))
                self.db.commit()
                # Ambil ID karyawan dari informasi login
                id_karyawan = user_info["id"]
                # Ambil ID pembeli dari informasi login
                id_pembeli = user_info["id"]
                id_produk = item["id_produk"]

                # Tambahkan ke histori pembelian
                query = "INSERT INTO transaksi (id_transaksi, waktu_transaksi, id_karyawan, id_produk, id_pembeli) VALUES ('', %s, %s, %s, %s)"
                values = (datetime.now(), id_karyawan, id_produk, id_pembeli)
                self.cursor.execute(query, values)
                self.db.commit()

            print("Pembelian berhasil. Terima kasih atas pembelian Anda!")
        except mysql.connector.Error as err:
            print("Error saat memproses transaksi:", err)

    def tampilkan_invoice(self):
        if self.invoice:
            print(f"{'-'*40:^40}")
            print(f"{'INVOICE PEMBELIAN':^40}")
            print(f"{'-'*40:^40}")
            table = PrettyTable()
            table.field_names = ["ID Produk", "Nama Produk", "Merk",
                                 "Jumlah", "Harga Satuan", "Biaya Pemasangan", "Total Harga"]

            for item in self.invoice:
                total_harga = item["jumlah"] * \
                    (item["harga_satuan"] + item["biaya_pemasangan"])
                table.add_row([
                    item["id_produk"],
                    item["nama_produk"],
                    item["merk"],
                    item["jumlah"],
                    item["harga_satuan"],
                    item["biaya_pemasangan"],
                    total_harga
                ])

            print(table)
        else:
            print("Tidak ada item dalam invoice saat ini.")

    def beli(self):
        self.invoice = []
        total_pembelian = 0
        while True:
            try:
                product_id = int(
                    input("Masukkan ID Produk yang ingin dibeli (atau 0 untuk keluar): "))
                if product_id == 0:
                    break

                query = "SELECT * FROM produk WHERE id_produk = %s"
                self.cursor.execute(query, (product_id,))
                product = self.cursor.fetchone()

                if not product:
                    print("Produk dengan ID tersebut tidak ditemukan.")
                    continue

                jumlah = int(
                    input(f"Masukkan jumlah {product[1]} (merk {product[2]}) yang ingin dibeli: "))

                if jumlah <= 0:
                    print("Jumlah produk tidak boleh 0 atau negatif.")
                    continue

                if jumlah > product[3]:
                    print("Stok tidak mencukupi.")
                    continue

                for item in self.invoice:
                    if item["id_produk"] == product_id:
                        item["jumlah"] += jumlah
                        break
                else:
                    self.invoice.append({
                        "id_produk": product[0],
                        "nama_produk": product[1],
                        "merk": product[2],
                        "jumlah": jumlah,
                        "harga_satuan": product[4],
                        "biaya_pemasangan": product[5],
                    })

                total_pembelian += jumlah * (product[4] + product[5])
            except ValueError:
                print("Input tidak valid. Masukkan angka yang benar.")

        if self.invoice:
            self.tampilkan_invoice()
            while True:
                try:
                    print("Total Pembayaran: ", total_pembelian)
                    uang_bayar = float(
                        input("Masukkan jumlah uang yang dibayarkan: "))
                    if uang_bayar < total_pembelian:
                        print(
                            "Jumlah uang yang dibayarkan kurang dari total pembelian.")
                    else:
                        break
                except ValueError:
                    print("Input tidak valid. Masukkan angka yang benar.")

            kembalian = uang_bayar - total_pembelian
            print(f"Uang yang dibayarkan: {uang_bayar}")
            print(f"Kembalian: {kembalian}")

            konfirmasi = input(
                "Apakah Anda ingin membayar pembelian ini? (y/n): ").lower()
            if konfirmasi == 'y':
                self.simpan_transaksi()
                print("Total Pembayaran: ", total_pembelian)
            elif konfirmasi == 'n':
                self.beli()
            else:
                print(
                    "Pilihan tidak valid. Silakan pilih 'y' untuk membayar atau 'n' untuk membatalkan.")
                self.beli()
        else:
            print("Pembelian dibatalkan.")

    @staticmethod
    def search(cursor):
        print(f"{'-'*40:^40}")
        print(f"{'SEARCH':^40}")
        print(f"{'-'*40:^40}")
        while True:
            search = input(
                "Masukkan nama produk atau merk yang ingin dicari: ")
            try:
                query = "SELECT * FROM produk WHERE nama_produk LIKE %s OR merk LIKE %s"
                cursor.execute(query, (f"%{search}%", f"%{search}%"))
                results = cursor.fetchall()
                if search.strip():
                    if cursor.rowcount != 0:
                        table = PrettyTable()
                        table.field_names = [
                            "ID Produk", "Nama Produk", "Merk", "Stok", "Harga Produk", "Biaya Pemasangan"]

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

    @staticmethod
    def sort_murah(cursor):
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
            table.field_names = ["ID Produk", "Nama Produk",
                                 "Merk", "Stok", "Harga Produk", "Biaya Pemasangan"]

            for row in results:
                table.add_row(row)

            print(table)
        except mysql.connector.Error as err:
            print("Error:", err)

    @staticmethod
    def sort_mahal(cursor):
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
            table.field_names = ["ID Produk", "Nama Produk",
                                 "Merk", "Stok", "Harga Produk", "Biaya Pemasangan"]

            for row in results:
                table.add_row(row)

            print(table)
        except mysql.connector.Error as err:
            print("Error:", err)

# Penjelasan
Class Pembeli berfungsi untuk mencangkup fungsi dari pembeli seperti beli produk, lihat produk, menampilkan invoice, simpan transaksi, search produk, sortir produk dari mahal ke murah, dan sortir produk dari murah ke mahal. 

# def login
    def login():
        global user_info
        print(f"{'-'*40:^40}")
        print(f"{'MENU LOGIN':^40}")
        print(f"{'-'*40:^40}")
        while True:
            username = input("Username: ")
            password = pwinput.pwinput("Password: ")
            if username and password:
                query = "SELECT * FROM pembeli WHERE BINARY username = %s AND password = %s"
                cursor.execute(query, (username, password))
                pembeli = cursor.fetchone()
                if pembeli:
                    print("Login berhasil sebagai pembeli.")
                    user_info = {"role": "pembeli", "id": pembeli[0]}
                    menu_pembeli()
                    break
                else:
                    query = "SELECT * FROM karyawan WHERE username = %s AND password = %s"
                    cursor.execute(query, (username, password))
                    karyawan = cursor.fetchone()
                    if karyawan:
                        print("Login berhasil sebagai karyawan.")
                        user_info = {"role": "karyawan", "id": karyawan[0]}
                        menu_karyawan()
                        break
                    else:
                        print("Username atau password salah. Silakan coba lagi.")
            else:
                print("Username dan password harus diisi.")

## Penjelasn
User dapat login dengan memasukkan username dan password. Jika login berhasil, user akan diarahkan ke menu sesuai dengan perannya, baik sebagai pembeli maupun karyawan.
                
# def register
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
                tanggal_lahir = input(
                    "Masukkan tanggal lahir (format: YYYY-MM-DD): ")
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
                    cursor.execute(query, (nama, jenis_kelamin, tgl,
                                   kota, alamat, username, password))
                    db.commit()
                    print("Berhasil Register!")
                    menu_pembeli()
                    break
                break
            except:
                print("Invalid Data")

## Penjelasan
User yang belum memiliki akun dapat membuat akun baru dengan mengisi informasi pribadi, seperti nama lengkap, jenis kelamin, tanggal lahir, kota, alamat, username, dan password.

# def main_menu
    def main_menu():
        try:
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
                    if pilih == '1':
                        login()
                    elif pilih == '2':
                        register()
                    elif pilih == '3':
                        exit()
                else:
                    print("Input salah, silahkan pilih antara 1, 2 dan 3.")
        except KeyboardInterrupt:
            print("\nTerima kasih telah menggunakan program ini. Sampai jumpa!")
## Penjelasan
berfungsi untuk menu utama dari program.

# def menu_karyawan
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
                LinkedListProduk.tambah_produk()

            elif pilihan == 2:
                display_produk()

            elif pilihan == 3:
                id_produk = int(
                    input("Masukkan ID produk yang ingin diperbarui: "))
                LinkedListProduk.update(id_produk)

            elif pilihan == 4:
                id_produk = int(
                    input("Masukkan ID produk yang ingin dihapus: "))
                LinkedListProduk.hapus_produk(id_produk)
            elif pilihan == 5:
                print("Keluar dari Menu Kelola Produk.")
                break

            else:
                print("Pilihan tidak valid. Masukkan angka antara 1 dan 5.")

        except ValueError:
            print("Input tidak valid. Masukkan angka.")

## Penjelasan
Berfungsi untuk jika user yang login adalah karaywan maka menu yang ditampilkan adalah fungsi di atas.

# def pembeli
    def menu_pembeli():
        pembeli = Pembeli(cursor, db)  # Buat objek Pembeli di dalam menu_pembeli
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
                pembeli.beli()
                pembeli.tampilkan_invoice()
            elif pilihan == 2:
                display_produk()
            elif pilihan == 3:
                pembeli.sort_murah(cursor)
            elif pilihan == 4:
                pembeli.sort_mahal(cursor)
            elif pilihan == 5:
                pembeli.search(cursor)
            elif pilihan == 6:
                break
            else:
                print("Pilihan tidak valid.")

        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

## Penjelasan
Berfungsi untuk jika user yang login adalah pembeli maka menu yang ditampilkan adalah fungsi di atas.

# Koneksi database
    db = mysql.connector.connect(
        host="sql6.freesqldatabase.com",
        user="sql6702194",
        password="t6ayvq7vPm",
        database="sql6702194"
    )
    
    cursor = db.cursor()
