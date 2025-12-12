import random
import math

# Fungsi untuk mengecek apakah bilangan prima
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Fungsi untuk menghasilkan bilangan prima acak dalam rentang 50-200
def generate_random_prime(min_val=50, max_val=200):
    primes = [i for i in range(min_val, max_val + 1) if is_prime(i)]
    return random.choice(primes)

# Fungsi untuk menghitung GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Fungsi untuk menghitung invers modular menggunakan Extended Euclidean Algorithm
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("Invers tidak ada")
    return x % phi

# Program utama RSA
def rsa_program():
    print("=== Program RSA dengan p, q, e Acak ===")
    
    # Langkah 1: Pilih p dan q secara acak dari prima 50-200
    p = generate_random_prime()
    q = generate_random_prime()
    while p == q:  # Pastikan p != q
        q = generate_random_prime()
    
    print(f"Langkah 1: Bilangan prima p dipilih acak: {p}")
    print(f"Langkah 1: Bilangan prima q dipilih acak: {q}")
    
    # Langkah 2: Hitung n = p * q
    n = p * q
    print(f"Langkah 2: n = p * q = {p} * {q} = {n}")
    
    # Langkah 3: Hitung φ(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)
    print(f"Langkah 3: φ(n) = (p-1) * (q-1) = ({p}-1) * ({q}-1) = {p-1} * {q-1} = {phi_n}")
    
    # Langkah 4: Pilih e secara acak, 1 < e < φ(n), dan gcd(e, φ(n)) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)
    print(f"Langkah 4: e dipilih acak: {e} (memastikan gcd({e}, {phi_n}) = 1)")
    
    # Langkah 5: Hitung d sebagai invers modular e modulo φ(n)
    d = mod_inverse(e, phi_n)
    print(f"Langkah 5: d = invers modular e modulo φ(n) = {d} (karena {e} * {d} ≡ 1 mod {phi_n})")
    
    # Kunci publik dan privat
    public_key = (e, n)
    private_key = (d, n)
    print(f"Kunci Publik: {public_key}")
    print(f"Kunci Privat: {private_key}")
    
    # Input plaintext sebagai bilangan bulat m (untuk kesederhanaan, asumsikan m < n)
    m = int(input(f"Masukkan plaintext m (bilangan bulat positif < {n}): "))
    if not (0 < m < n):
        print("Error: m harus 0 < m < n")
        return
    
    print(f"Plaintext m: {m}")
    
    # Langkah 6: Enkripsi c = m^e mod n
    c = pow(m, e, n)
    print(f"Langkah 6: Enkripsi - c = m^e mod n = {m}^{e} mod {n} = {c}")
    
    # Langkah 7: Dekripsi m_decrypted = c^d mod n
    m_decrypted = pow(c, d, n)
    print(f"Langkah 7: Dekripsi - m_decrypted = c^d mod n = {c}^{d} mod {n} = {m_decrypted}")
    
    # Verifikasi
    if m == m_decrypted:
        print("Verifikasi: Dekripsi berhasil! m == m_decrypted")
    else:
        print("Error: Dekripsi gagal!")

# Jalankan program
rsa_program()
