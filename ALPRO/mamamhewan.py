p_ayam = 0.5
p_kambing = 3.5
p_sapi = 5

jml_hari = int(input("untuk mamam berapa hari?"))
jml_ayam = int(input("\nMasukkan jumlah Ayam :"))
jml_kambing = int(input("Masukkan jumlah Kambing:"))
jml_sapi = int(input("Masukkan jumlah Sapi:"))

total_payam = (jml_ayam * p_ayam * jml_hari)
total_pkambing = (jml_kambing * p_kambing * jml_hari)
total_psapi = (jml_sapi * p_sapi * jml_hari)

print(f"Total Pakan Ayam :{total_payam}\nTotal Pakan Kambing:{total_pkambing}\nTotal Pakan Sapi:{total_psapi}")