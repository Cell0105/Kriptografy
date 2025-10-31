def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext.upper():
        if char in aturan:
            ciphertext += aturan[char]
        else:
            ciphertext += char
    return ciphertext

def buat_aturan_substitusi():
    aturan = {}
    print("Masukkan aturan substitusi (format: huruf_asal:huruf_ganti, contoh: A:B).")
    print("Ketik 'selesai' untuk berhenti memasukkan aturan.")
    
    while True:
        input_user = input("Masukkan aturan: ").strip().upper()
        if input_user == 'SELESAI':
            break
        if ':' in input_user:
            bagian = input_user.split(':')
            if len(bagian) == 2 and len(bagian[0]) == 1 and len(bagian[1]) == 1:
                huruf_asal, huruf_ganti = bagian
                aturan[huruf_asal] = huruf_ganti
                print(f"Aturan ditambahkan: {huruf_asal} -> {huruf_ganti}")
            else:
                print("Format salah. Gunakan format huruf_asal:huruf_ganti (contoh: A:B).")
        else:
            print("Format salah. Gunakan format huruf_asal:huruf_ganti (contoh: A:B).")
    
    return aturan


print("Program Substitusi Cipher")
plaintext = input("Masukkan plaintext: ").upper()
aturan_substitusi = buat_aturan_substitusi()

ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

print(f'\nPlaintext: {plaintext}')
print(f'Ciphertext: {ciphertext}')
