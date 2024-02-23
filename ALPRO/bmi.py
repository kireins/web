
data_pasien = []

while True:
    print("\n Kalkulator BMI ")
    print("\n1. Input Data Pasien")
    print("2. Hitung BMI Pasien")
    print("3. Exit.")
   
    pilih_menu = input("Menu: ")
   
    if pilih_menu == '1':
        nama_pasien = input("Masukkan nama pasien: ")
        bb_pasien = (input("Masukkan berat badan pasien (kg): "))
        tb_pasien = (input("Masukkan tinggi badan pasien (cm): "))

        if bb_pasien.isdigit() and tb_pasien.isdigit():
           bb = int(bb_pasien)
           tb = int(tb_pasien)
           data_pasien.append((nama_pasien,bb,tb))
           print("Data berhasil di simpan")
        else:
         print("Pilihan tidak valid. Silahkan pilih menu yang valid.")

    elif pilih_menu == '2':
       print("\nDaftar Data Pasien: ")
       print("No.     | Nama          | Berat Badan (kg)          | Tinggi Badan (cm)          ")
       for i, data in enumerate(data_pasien, start=1):
           print(f"{i}.          | {data[0]:<10} | {data[1]:<12} | {data[2]:<9} ")

       nomor_pasien = input("Pilih nomor pasien yang ingin di hitung BMI: ")

       if nomor_pasien.isdigit() and 1 <= int(nomor_pasien) <= len(nomor_pasien):
            index = int(nomor_pasien) - 1
            nama_pasien, bb, tb = data_pasien[index]
            bmi = bb / (tb / 100) ** 2
            if bmi < 18.5:
                kategori = "Underweight"
            elif 18.5 <= bmi < 25:
                kategori= "Normal"
            elif 25 <= bmi < 30:
                kategori = "Overweight"
            else:
                kategori = "Obesitas"

            print(f"/n{nama_pasien} memiliki BMI {bmi:.2f} dan termasuk dalam kategori {kategori}")

       else:
            print("Invalid patient number. Please enter a valid number.")

    elif pilih_menu == '3':
        print("Terima kasih sudah menggunakan kalkulator BMI <3!")
        break

