# Membaca jumlah kursi
N = int(input())

# Membaca status kursi
S = input()

# Variabel untuk menyimpan nomor kursi terbaik dan jarak maksimal
nomor_terbaik = -1
jarak_maksimal = -1

# Iterasi setiap kursi untuk mencari kursi kosong ('K')
for i in range(N):
    if S[i] == 'K':
        # Hitung jarak ke kursi terisi terdekat
        jarak_kiri = jarak_kanan = N  # Inisialisasi jarak sebagai nilai maksimal

        # Cari kursi terisi terdekat ke kiri
        for j in range(i, -1, -1):
            if S[j] == 'T':
                jarak_kiri = i - j
                break

        # Cari kursi terisi terdekat ke kanan
        for j in range(i, N):
            if S[j] == 'T':
                jarak_kanan = j - i
                break

        # Jarak minimum dari kedua arah
        jarak = min(jarak_kiri, jarak_kanan)

        # Pilih kursi jika jaraknya lebih besar atau sama dengan jarak maksimal yang ditemukan sebelumnya
        if jarak > jarak_maksimal:
            jarak_maksimal = jarak
            nomor_terbaik = i + 1  # Tambahkan 1 karena indeks dimulai dari 0

# Cetak nomor kursi terbaik atau "Penuh" jika tidak ada kursi kosong
if nomor_terbaik == -1:
    print("Penuh")
else:
    print(nomor_terbaik)
