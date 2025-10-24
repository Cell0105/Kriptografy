
print("Selamat datang di Kalkulator Sederhana!")
print("Program ini menggunakan operator aritmatika: +, -, *, /")


try:
    a = float(input("Masukkan nilai a: "))
except ValueError:
    print("Error: Nilai a harus berupa angka.")
    exit()  

# Input nilai b
try:
    b = float(input("Masukkan nilai b: "))
except ValueError:
    print("Error: Nilai b harus berupa angka.")
    exit() 


operator = input("Masukkan operator (+, -, *, /): ")


if operator == '+':
    hasil = a + b
    print("Hasil penambahan: ", hasil)
elif operator == '-':
    hasil = a - b
    print("Hasil pengurangan: ", hasil)
elif operator == '*':
    hasil = a * b
    print("Hasil perkalian: ", hasil)
elif operator == '/':
    if b != 0:
        hasil = a / b
        print("Hasil pembagian: ", hasil)
    else:
        print("Error: Pembagian oleh nol tidak diperbolehkan.")
else:
    print("Error: Operator tidak valid. Gunakan +, -, *, atau /.")

print("Terima kasih telah menggunakan kalkulator.")
