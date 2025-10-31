import itertools

def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

def kombinasi(n, r):
    if r > n or r < 0:
        return 0
    faktorial_n = faktorial(n)
    faktorial_r = faktorial(r)
    faktorial_n_r = faktorial(n - r)
    return faktorial_n // (faktorial_r * faktorial_n_r)


def generate_kombinasi(objek, r):
    return list(itertools.combinations(objek, r))


print("Program Kombinasi: Menghitung dan Menampilkan Kombinasi Objek")
n = int(input("Masukkan jumlah total objek (n): "))
r = int(input("Masukkan jumlah objek yang dipilih (r): "))


objek = [chr(65 + i) for i in range(n)]  
print(f"Objek yang digunakan: {objek}")


jumlah = kombinasi(n, r)
print(f"Jumlah kombinasi C({n}, {r}) adalah: {jumlah}")

if jumlah > 1000:
    print("Jumlah kombinasi terlalu besar untuk ditampilkan semua. Hanya menampilkan jumlah.")
else:
    kombinasi_list = generate_kombinasi(objek, r)
    print("Semua kombinasi:")
    for combo in kombinasi_list:
        print(f"  {list(combo)}")
