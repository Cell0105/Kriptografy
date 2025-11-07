mapping = {
    'U': 'K',
    'N': 'N',
    'I': 'I',
    'K': 'K',
    'A': 'B'
}

def substitute(plaintext, mapping):
    pt = plaintext.replace(" ", "")
    return "".join(mapping.get(ch, ch) for ch in pt)

def transposition_into_4blocks(text):
    # hitung panjang tiap blok = total karakter dibagi 4
    part_len = len(text) // 4
    if part_len == 0:
        part_len = 1

    parts = [text[i:i+part_len] for i in range(0, len(text), part_len)]

    max_col = max(len(p) for p in parts)

    ciphertext = ""
    for col in range(max_col):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]

    return parts, ciphertext

def main():
    plaintext = "UNIKA SANTO THOMAS"
    print("Plaintext:")
    print(plaintext)
    print()

    substituted = substitute(plaintext, mapping)
    print("Ciphertext setelah Substitusi:")
    print(substituted)
    print()

    parts, transposed = transposition_into_4blocks(substituted)
    print("Pembagian menjadi 4 bagian (blok):")
    for i, p in enumerate(parts, start=1):
        print(f"Bagian {i}: '{p}'")
    print()

    print("Proses pembentukan ciphertext dari tiap kolom:")
    max_col = max(len(p) for p in parts)
    step_list = []
    for col in range(max_col):
        for idx, part in enumerate(parts, start=1):
            if col < len(part):
                ch = part[col]
                step_list.append((col+1, idx, ch))
                print(f"Menambahkan '{ch}' dari Bagian {idx} (kolom {col+1})")
    print()

    print("Ciphertext setelah Substitusi + Transposisi:")
    print(transposed)

if __name__ == "__main__":
    main()
