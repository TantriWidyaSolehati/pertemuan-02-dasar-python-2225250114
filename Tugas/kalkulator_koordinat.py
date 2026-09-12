#INPUT TITIK A
x1 = float(input("Masukkan koordinat x titik A: "))
y1 = float(input("Masukkan koordinat y titik A: "))

#INPUT TITIK B
x2 = float(input("Masukkan koordinat x titik B: "))
y2 = float(input("Masukkan koordinat y titik B: "))


titik_A = (x1, y1)
titik_B = (x2, y2)

#PERUBAHAN KOORDINAT
dx = (x2 - x1)
dy = (y2 - y1)

#HITUNG JARAK
jarak = ((dx)**2 + (dy)**2)**0.5
titik_tengah = ((x1 + x2) / 2, (y1 + y2) / 2)

#OUTPUT
print("Koordinat titik A: ", f"({titik_A[0]:.2f}, {titik_A[1]:.2f})")
print("Koordinat titik B: ", f"({titik_B[0]:.2f}, {titik_B[1]:.2f})")
print("Perubahan: ", f"({dx:.2f}, {dy:.2f})")
print("Jarak antara titik A dan B: ", f"{jarak:.2f}")
print("Titik tengah antara titik A dan B: ", f"({titik_tengah[0]:.2f}, {titik_tengah[1]:.2f})")