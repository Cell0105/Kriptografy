import operator


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

while True:
    # Input nilai
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = input("Masukkan operator (+, -, *, /): ")

    try:
        hasil = ops[c](a, b)
        print(f"Hasil dari {a} {c} {b} = {hasil}")
    except KeyError:
        print("Operator tidak valid.")
    except ZeroDivisionError:
        print("Pembagian dengan nol tidak diperbolehkan.")

    # Tanya apakah ingin lanjut
    ulang = input("Apakah Anda ingin memulai operasi perhitungan lagi? (y/n): ").lower()
    if ulang != 'y':
        break

# Contoh tambahan sederhana
a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))
c = a + b
print("Hasil dari Nilai C adalah:", c)

print("Program selesai. Terima kasih!")
