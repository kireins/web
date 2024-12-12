kaki_kambing = 4
kaki_ayam = 2
kaki_sapi = 4

print("Perhitungan Hewan di Peternakan")

jml_ayam = int(input("Masukkan jumlah Ayam :"))
jml_kambing = int(input("Masukkan jumlah Kambing:"))
jml_sapi = int(input("Masukkan jumlah Sapi:"))

total_hewan = (jml_ayam * kaki_ayam) + (jml_kambing * kaki_kambing) + (jml_sapi * kaki_sapi)


print(f"Jumlah hewan ternak: {total_hewan}")