import sqlite3

# Membuat koneksi ke database (jika tidak ada, akan dibuat)
conn = sqlite3.connect('inventaris_buku.db')
cursor = conn.cursor()

# Membuat tabel buku
cursor.execute('''
CREATE TABLE IF NOT EXISTS buku (
    id_buku INTEGER PRIMARY KEY,
    judul TEXT NOT NULL,
    penulis TEXT NOT NULL,
    genre TEXT NOT NULL,
    tahun_terbit INTEGER NOT NULL,
    stok INTEGER NOT NULL
)
''')

print("Tabel buku berhasil dibuat.")

# Menutup koneksi
conn.close()
