import itertools


def permutasi_menyeluruh(arr):
    return list(itertools.permutations(arr))

def permutasi_sebagian(arr, k):
    return list(itertools.permutations(arr, k))

def permutasi_keliling(arr):
    if len(arr) == 1:
        return [arr]
    pertama = arr[0]
    permutasi_penuh = list(itertools.permutations(arr[1:]))
    return [[pertama] + list(perm) for perm in permutasi_penuh]

def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil


def latihan_2_hitung_jumlah(n, r):
    jumlah_cara = r ** n
    print(f"Jumlah cara mengatur {n} buku di {r} bagian rak: {jumlah_cara}")
    print("(Catatan: Setiap buku dipilih bagian secara independen, bagian bisa kosong.)")
    return jumlah_cara



while True:
    print("\n=== Menu Program Permutasi dan Latihan ===")
    print("1. Permutasi Menyeluruh")
    print("2. Permutasi Sebagian")
    print("3. Permutasi Keliling")
    print("4. Permutasi Berkelompok")
    print("5. Latihan 2: Mengatur n Buku (Hitung Jumlah Saja)")
    print("6. Keluar")
    
    pilihan = input("Masukkan pilihan (1-6): ").strip()
    
    if pilihan == '1':
        arr_input = input("Masukkan elemen (pisahkan dengan spasi): ").strip()
        arr = arr_input.split()
        hasil = permutasi_menyeluruh(arr)
        print("Permutasi Menyeluruh:", hasil)

    elif pilihan == '2':
        arr_input = input("Masukkan elemen (pisahkan dengan spasi): ").strip()
        arr = arr_input.split()
        k = int(input("Masukkan k: ").strip())
        hasil = permutasi_sebagian(arr, k)
        print("Permutasi Sebagian:", hasil)

    elif pilihan == '3':
        arr_input = input("Masukkan elemen (pisahkan dengan spasi): ").strip()
        arr = arr_input.split()
        hasil = permutasi_keliling(arr)
        print("Permutasi Keliling:", hasil)

    elif pilihan == '4':
        r = int(input("Masukkan jumlah kelompok: ").strip())
        grup = []
        for i in range(r):
            kelompok_input = input(f"Masukkan elemen kelompok {i+1}: ").strip()
            kelompok = kelompok_input.split()
            grup.append(kelompok)
        hasil = permutasi_berkelompok(grup)
        print("Permutasi Berkelompok:", hasil)

    elif pilihan == '5':
        n = int(input("Masukkan n (jumlah buku): ").strip())
        r = int(input("Masukkan r (jumlah bagian rak): ").strip())
        latihan_2_hitung_jumlah(n, r)

    elif pilihan == '6':
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-6.")
