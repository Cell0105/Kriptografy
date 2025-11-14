import numpy as np

def text_to_binary_table(text):
    """
    Mengonversi teks menjadi tabel biner 8-bit per karakter.
    Jika teks kurang dari 8 karakter, tambahkan "SPASI" dengan biner 00000000.
    """
    binary_table = []
    for char in text:
        binary_code = format(ord(char), '08b')
        binary_table.append((char.upper(), binary_code))
    for _ in range(8 - len(text)):
        binary_table.append(("SPASI", "00000000"))
    return binary_table

def print_binary_table(binary_table):
    """
    Mencetak tabel biner.
    """
    print("Key (huruf kecil)\tBiner")
    for key, biner in binary_table:
        print(f"{key}\t\t{biner}")

def apply_permutation(bits, permutation_table):
    """
    Menerapkan permutasi pada list bits berdasarkan tabel permutasi.
    """
    return [bits[pos - 1] for pos in permutation_table]

def left_shift(bits, shift_amount):
    """
    Melakukan left shift pada list bits.
    """
    return bits[shift_amount:] + bits[:shift_amount]

def generate_subkeys(C0, D0, shifts, PC_2):
    """
    Menghasilkan subkunci K1 hingga K16 menggunakan C dan D.
    """
    C_values = [C0]
    D_values = [D0]
    K_values = []
    
    for shift in shifts:
        C_prev = C_values[-1]
        D_prev = D_values[-1]
        C_new = left_shift(C_prev, shift)
        D_new = left_shift(D_prev, shift)
        C_values.append(C_new)
        D_values.append(D_new)
        
        # Gabungkan C dan D
        combined = C_new + D_new
        # Terapkan PC-2
        K = [combined[pos - 1] for pos in PC_2.flatten()]
        K_values.append(K)
    
    return C_values, D_values, K_values

def print_matrix(bits, label, cols=7):
    """
    Mencetak bits dalam format matriks dengan kolom tertentu.
    """
    print(f"\n{label}:")
    for i in range(0, len(bits), cols):
        print(' '.join(map(str, bits[i:i + cols])))

def print_C_D_K(C_values, D_values, K_values):
    """
    Mencetak nilai C, D, dan K.
    """
    for i in range(17):
        print(f"C{i}: {' '.join(map(str, C_values[i]))}")
        print(f"D{i}: {' '.join(map(str, D_values[i]))}")
        if i < 16:
            print(f"K{i+1}: {' '.join(map(str, K_values[i]))}")
        print()

# Definisi tabel permutasi
PC_1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

PC_2 = np.array([
    [14, 17, 11, 24, 1, 5],
    [3, 28, 15, 6, 21, 10],
    [23, 19, 12, 4, 26, 8],
    [16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55],
    [30, 40, 51, 45, 33, 48],
    [44, 49, 39, 56, 34, 53],
    [46, 42, 50, 36, 29, 32]
])

# Shift amounts untuk setiap ronde
shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Eksekusi utama
if __name__ == "__main__":
    # Bagian 1: Konversi teks ke biner
    text = "marto"
    binary_table = text_to_binary_table(text)
    print_binary_table(binary_table)
    
    # Bagian 2: Persiapan kunci
    key_str = "0110110101100001011100100111010001101111000000000000000000000000"
    key_bits = [int(bit) for bit in key_str]
    
    print("\nKunci Awal:")
    for i in range(0, 64, 8):
        print(' '.join(map(str, key_bits[i:i + 8])))
    
    # Terapkan PC-1
    permuted_key = apply_permutation(key_bits, PC_1)
    print_matrix(permuted_key, "Permutasi PC-1 (Matriks 8x7)", cols=7)
    
    # Bagi menjadi C0 dan D0
    C0 = permuted_key[:28]
    D0 = permuted_key[28:]
    print_matrix(C0, "C0", cols=7)
    print_matrix(D0, "D0", cols=7)
    
    # Bagian 3: Generate subkunci
    C_values, D_values, K_values = generate_subkeys(C0, D0, shifts, PC_2)
    print_C_D_K(C_values, D_values, K_values)
