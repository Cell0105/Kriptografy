import math

# --- 1. Definisi Kunci RSA Tetap ---
p = 17
q = 11
e = 7  # Kunci Publik

# --- 2. Perhitungan Kunci Utama ---
n = p * q
phi_n = (p - 1) * (q - 1)

# Fungsi untuk menghitung Invers Modular (Kunci Privat d)
def extended_gcd(a, b):
    # Algoritma Euclidean Diperluas
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    # Menghitung d sehingga (d * a) % m == 1
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Invers modular tidak ada. Pilih nilai e yang berbeda.')
    else:
        return (x % m + m) % m

# --- 3. Menghitung Kunci Privat (d) ---
try:
    d = mod_inverse(e, phi_n)
except Exception as error:
    print(f"Error: {error}")
    exit()

print("====================================")
print("🔑 Konfigurasi Kunci RSA (p=17, q=11, e=7)")
print(f"Modulus (n): {n}")
print(f"Totient (phi(n)): {phi_n}")
print(f"Kunci Publik (e, n): ({e}, {n})")
print(f"Kunci Privat (d, n): ({d}, {n})")
print("====================================\n")

# --- 4. Fungsi Enkripsi dan Dekripsi ---

def rsa_encrypt(m, e, n):
    """Menghitung Ciphertext: c = m^e mod n"""
    # Menggunakan fungsi pow(base, exp, mod) yang sangat efisien di Python
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    """Menghitung Pesan Asli: m = c^d mod n"""
    return pow(c, d, n)

# --- 5. Input Pengguna dan Proses ---

while True:
    try:
        # Batasan pesan harus kurang dari n (187)
        m_input = int(input(f"Masukkan pesan M (bilangan bulat positif < {n}): "))
        if 0 < m_input < n:
            break
        else:
            print(f"Error: Pesan harus lebih besar dari 0 dan kurang dari {n}.")
    except ValueError:
        print("Error: Masukkan harus berupa bilangan bulat.")


# a. Enkripsi
C = rsa_encrypt(m_input, e, n)
print(f"\n--- ENKRIPSI ---")
print(f"Pesan Asli (M): {m_input}")
print(f"Ciphertext (C = M^{e} mod {n}): {C}")

# b. Dekripsi
M_decrypted = rsa_decrypt(C, d, n)
print(f"\n--- DEKRIPSI ---")
print(f"Ciphertext (C): {C}")
print(f"Pesan Dekripsi (M = C^{d} mod {n}): {M_decrypted}")

if m_input == M_decrypted:
    print("\n✅ Proses RSA Berhasil Dikonfirmasi.")
else:
    print("\n❌ Proses RSA Gagal.")