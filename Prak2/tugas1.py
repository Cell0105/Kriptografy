def evaluate_expression(expr):
    # Hapus spasi dari ekspresi
    expr = expr.replace(" ", "")
    
    # Parse token: angka dan operator
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit() or (expr[i] == '.' and i+1 < len(expr) and expr[i+1].isdigit()):
            # Bangun angka (termasuk desimal)
            num = ''
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                num += expr[i]
                i += 1
            tokens.append(num)
        else:
            # Operator
            tokens.append(expr[i])
            i += 1
    
    # Evaluasi dari kiri ke kanan tanpa prioritas operator
    if not tokens:
        return 0.0
    
    result = float(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        if i + 1 >= len(tokens):
            break  # Error, tapi untuk sederhana, abaikan
        num = float(tokens[i+1])
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            if num != 0:
                result /= num
            else:
                raise ValueError("Division by zero")
        i += 2
    
    return result

# Contoh penggunaan
def main():
    print("Kalkulator Hybrid")
    print("Masukkan ekspresi matematika (contoh: 4+4–3 atau 5 – 3 * 4)")
    print("Ketik 'exit' untuk keluar.")
    
    while True:
        expr = input("Input (Ekspresi): ")
        if expr.lower() == 'exit':
            break
        try:
            result = evaluate_expression(expr)
            print(f"Hasil Diproses: {expr.replace(' ', '')}")  # Tampilkan ekspresi tanpa spasi
            print(f"Output (Hasil): {int(result) if result.is_integer() else result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
