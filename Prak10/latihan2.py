import random
import math

def is_prime(n):
    """Fungsi sederhana untuk mengecek apakah n adalah bilangan prima."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_generator(p):
    """Cari generator g untuk prima p."""
    for g in range(2, p):
        if all(pow(g, (p-1)//q, p) != 1 for q in [2, 3, 5] if q < p):  # Cek sederhana
            return g
    return 2  # Fallback

def generate_keys(p, g, x):
    """Generate public key y = g^x mod p."""
    y = pow(g, x, p)
    return y

def encrypt(p, g, y, m, k):
    """Enkripsi pesan m menggunakan public key y dan k yang diberikan."""
    if not (0 < m < p):
        raise ValueError("Pesan m harus antara 1 dan p-1.")
    if not (1 <= k < p-1):
        raise ValueError("k harus antara 1 dan p-2.")
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    return c1, c2

def decrypt(p, x, c1, c2):
    """Dekripsi ciphertext (c1, c2) menggunakan private key x."""
    s = pow(c1, x, p)
    s_inv = pow(s, p-2, p)  # Invers modulo p
    m = (c2 * s_inv) % p
    return m

def main():
    print("Program Algoritma ElGamal (Angka Acak, Pesan sebagai Kata/Kalimat, K Input User)")
    print("=================================================================================")
    
    # Generate p secara acak (bilangan prima antara 1000 dan 10000, tapi bisa diperbesar jika perlu)
    p = random.randint(1000, 10000)
    while not is_prime(p):
        p = random.randint(1000, 10000)
    
    # Generate g sebagai generator
    g = find_generator(p)
    
    # Generate x secara acak
    x = random.randint(1, p-2)
    
    # Generate public key
    y = generate_keys(p, g, x)
    
    print(f"Bilangan prima p (acak): {p}")
    print(f"Generator g (acak): {g}")
    print(f"Private key x (acak): {x}")
    print(f"Public key y: {y}")
    
    # Input pesan sebagai string
    m_str = input("Masukkan pesan (kata/kalimat): ")
    
    # Konversi string ke list ASCII desimal
    pesan_list = [ord(c) for c in m_str]
    
    # Validasi setiap karakter; jika ada yang >= p, regenerate p yang lebih besar
    max_ascii = max(pesan_list) if pesan_list else 0
    while max_ascii >= p:
        print(f"ASCII value maksimal {max_ascii} >= p ({p}). Regenerating p yang lebih besar...")
        p = random.randint(p + 1, p * 2)  # Perbesar p
        while not is_prime(p):
            p = random.randint(p + 1, p * 2)
        g = find_generator(p)
        x = random.randint(1, p-2)
        y = generate_keys(p, g, x)
        print(f"New p: {p}, g: {g}, x: {x}, y: {y}")
    
    # Input K dari user
    k = int(input(f"Masukkan nilai k (1 <= k < {p-1}): "))
    if not (1 <= k < p-1):
        print(f"Error: k harus antara 1 dan {p-2}.")
        return
    
    # Enkripsi setiap karakter menggunakan k yang sama
    ciphertext_list = []
    for m in pesan_list:
        try:
            c1, c2 = encrypt(p, g, y, m, k)
            ciphertext_list.append((c1, c2))
        except ValueError as e:
            print(f"Error saat enkripsi: {e}")
            return
    
    print(f"Ciphertext (list of (c1, c2) per karakter): {ciphertext_list}")
    
    # Dekripsi setiap ciphertext
    decrypted_list = []
    for c1, c2 in ciphertext_list:
        try:
            decrypted_m = decrypt(p, x, c1, c2)
            decrypted_list.append(decrypted_m)
        except ValueError as e:
            print(f"Error saat dekripsi: {e}")
            return
    
    # Konversi kembali ke string
    decrypted_str = ''.join(chr(val) for val in decrypted_list)
    print(f"Pesan asli setelah dekripsi: '{decrypted_str}'")
    if decrypted_str == m_str:
        print("Dekripsi berhasil!")
    else:
        print("Dekripsi gagal.")

if __name__ == "__main__":
    main()