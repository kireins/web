import numpy as np

# Data biaya
no_makam = np.array(range(1, 11))
biaya_pemeliharaan_rutin = np.full(10, 200) 
biaya_tambahan = np.array([50, 0, 25, 100, 75, 50, 0, 20, 80,
60])
# Menghitung total tagihan per makam
total_tagihan_per_makam = biaya_pemeliharaan_rutin + biaya_tambahan
# Menghitung total tagihan keseluruhan
total_tagihan_keseluruhan = np.sum(total_tagihan_per_makam)
# Menentukan biaya tambahan tertinggi dan terendah
biaya_tambahan_tertinggi = np.max(biaya_tambahan)
biaya_tambahan_terendah = np.min(biaya_tambahan)
# Menghitung rata-rata biaya tambahan
rata_rata_biaya_tambahan = np.mean(biaya_tambahan)
# Menyimpan data dalam dictionary
tagihan_makam_dict = dict(zip(no_makam, total_tagihan_per_makam))

print("Total tagihan keseluruhan: ", total_tagihan_keseluruhan)
print("Biaya tambahan tertinggi: ", biaya_tambahan_tertinggi)
print("Biaya tambahan terendah: ", biaya_tambahan_terendah)
print("Rata-rata biaya tambahan: ", rata_rata_biaya_tambahan)
print("Tagihan per makam(dict): ", tagihan_makam_dict)