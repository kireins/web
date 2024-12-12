import numpy as np

tarifBulanan = np.array([1500000, 1500000, 1500000, 2000000, 1800000, 1800000, 2000000, 2000000])
tunggakan = np.array([0, 300000, 150000, 0, 0, 500000, 250000, 0])

print('-'* 20)
print("Selamat Datang Admin Budi Kost!")
print("Berikut adalah data Budi Kost")
print('-'* 20)


totalPemasukan = np.sum(tarifBulanan) - np.sum(tunggakan) * 0.05  
print("\nTotal Pemasukan Bulanan: Rp", totalPemasukan)

meanTarif = np.mean(tarifBulanan)
print("\nRata-rata Tarif Bulanan: Rp", meanTarif)

maxTunggakan = np.max(tunggakan) + 1
print("\nKamar dengan Tunggakan Tertinggi:", maxTunggakan)

totalTunggakan = np.sum(tunggakan)
print("\nTotal Tunggakan: Rp", totalTunggakan)

if totalTunggakan == 0:
    diskon = np.sum(tarifBulanan) * 0.05
    print("\nTotal Diskon: Rp", diskon)
else:
    print("Maaf, tidak ada diskon karena terdapat tunggakan.")
    
tagihan = {}
for i in range(len(tarifBulanan)):
    tagihan[f"Kamar {i+1}"] = {
        "Tarif Bulanan (Rp)": tarifBulanan[i],
        "Tunggakan (Rp)": tunggakan[i],
        "Diskon (Rp)": tarifBulanan[i] * 0.05 
        
        if tunggakan[i] == 0 

        else 0
    }
print("\nData Tagihan Budi Kost:")
print(tagihan)
