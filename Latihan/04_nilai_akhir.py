Nama = input("Masukan nama : ")
Nilai_tugas = float(input("Masukan nilai tugas : "))
Nilai_uts = float(input("Masukan nilai UTS : "))    
Nilai_uas = float(input("Masukan nilai UAS : "))
Nilai_akhir = (Nilai_tugas * 0.2) + (Nilai_uts * 0.3) + (Nilai_uas * 0.5)

print("Nilai akhir :", f"{Nilai_akhir:.2f}")