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

def generate_keys(p, g, x):
    """Generate public key y = g^x mod p."""
    if not is_prime(p):
        raise ValueError("p harus bilangan prima.")
    if not (1 < g < p):
        raise ValueError("g harus antara 1 dan p-1.")
    if not (1 <= x < p-1):
        raise ValueError("x harus antara 1 dan p-2.")
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
    print("Program Algoritma ElGamal (Pesan sebagai Kata/Kalimat, K Input User)")
    print("===================================================================")
    
    # Input dari user
    p = int(input("Masukkan bilangan prima p: "))
    g = int(input("Masukkan generator g (1 < g < p): "))
    x = int(input("Masukkan private key x (1 <= x < p-1): "))
    
    # Generate public key
    try:
        y = generate_keys(p, g, x)
        print(f"Public key y = {y}")
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    # Input pesan sebagai string
    m_str = input("Masukkan pesan (kata/kalimat): ")
    
    # Konversi string ke list ASCII desimal
    pesan_list = [ord(c) for c in m_str]
    
    # Validasi setiap karakter
    for val in pesan_list:
        if not (0 < val < p):
            print(f"Error: ASCII value {val} untuk karakter '{chr(val)}' tidak valid (harus 1 <= val < p). Pilih p yang lebih besar.")
            return
    
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