# 1. Membuat array (list) kosong untuk menyimpan daftar belanjaan
daftar_belanja = []
print(f"1. Daftar belanja awal: {daftar_belanja}")

# 2. Menambah item di akhir array (append)
daftar_belanja.append("Apel")
daftar_belanja.append("Roti")
daftar_belanja.append("Susu")
print(f"2. Setelah ditambah 3 item: {daftar_belanja}")

# 3. Mengakses elemen berdasarkan indeks (dimulai dari 0)
item_pertama = daftar_belanja[0]
print(f"3. Item pertama (indeks 0) adalah: {item_pertama}")

# 4. Mengubah nilai elemen pada indeks tertentu
# Ternyata kita mau Roti Tawar, bukan Roti biasa
daftar_belanja[1] = "Roti Tawar"
print(f"4. Setelah diubah, daftarnya menjadi: {daftar_belanja}")


# 5. Menambah item di posisi tertentu (insert)
# Menambahkan "Keju" di posisi kedua (indeks 1)
daftar_belanja.insert(1, "Keju")
print(f"5. Setelah disisipkan Keju: {daftar_belanja}")

# 6. Menghapus item berdasarkan nilainya (remove)
# Kita tidak jadi beli Apel
daftar_belanja.remove("Apel")
print(f"6. Setelah Apel dihapus: {daftar_belanja}")
