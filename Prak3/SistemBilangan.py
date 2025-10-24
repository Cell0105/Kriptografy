class sb:
    """Utility conversion class for number systems.

    Provides static methods to convert between binary, octal, decimal and
    hexadecimal. Methods accept strings for non-decimal inputs (they may
    include prefixes like '0b', '0o', '0x') and integers for decimal input.
    """

    @staticmethod
    def decToBin(value: int) -> str:
        return bin(int(value))[2:]

    @staticmethod
    def decToOctal(value: int) -> str:
        return oct(int(value))[2:]

    @staticmethod
    def decToHex(value: int) -> str:
        return hex(int(value))[2:].upper()

    # Binary -> Decimal, Hex
    @staticmethod
    def binToDec(b: str) -> int:
        s = str(b).strip()
        if s.startswith(('0b', '0B')):
            s = s[2:]
        if s == '' or any(ch not in '01' for ch in s):
            raise ValueError(f"Invalid binary number: {b!r}")
        return int(s, 2)

    @staticmethod
    def binToHex(b: str) -> str:
        return sb.decToHex(sb.binToDec(b))

    # Octal -> Decimal, Binary, Hex
    @staticmethod
    def octToDec(o: str) -> int:
        s = str(o).strip()
        if s.startswith(('0o', '0O')):
            s = s[2:]
        if s == '' or any(ch not in '01234567' for ch in s):
            raise ValueError(f"Invalid octal number: {o!r}")
        return int(s, 8)

    @staticmethod
    def octToBin(o: str) -> str:
        return sb.decToBin(sb.octToDec(o))

    @staticmethod
    def octToHex(o: str) -> str:
        return sb.decToHex(sb.octToDec(o))

    # Hex -> Decimal, Binary, Octal
    @staticmethod
    def hexToDec(h: str) -> int:
        s = str(h).strip()
        if s.startswith(('0x', '0X')):
            s = s[2:]
        if s == '' or any(ch not in '0123456789abcdefABCDEF' for ch in s):
            raise ValueError(f"Invalid hexadecimal number: {h!r}")
        return int(s, 16)

    @staticmethod
    def hexToBin(h: str) -> str:
        return sb.decToBin(sb.hexToDec(h))

    @staticmethod
    def hexToOct(h: str) -> str:
        return sb.decToOctal(sb.hexToDec(h))


def _demo():
    """Simple demo prints to verify conversions. This runs only when the
    module is executed directly and when the interactive menu isn't used.
    """
    examples = [
        ("binary", '1011'),
        ("octal", '17'),
        ("hex", '1F'),
    ]
    print("Demo conversions:")
    print(f"Binary 1011 -> Decimal: {sb.binToDec('1011')}")
    print(f"Binary 1011 -> Hex: {sb.binToHex('1011')}")
    print(f"Octal 17 -> Decimal: {sb.octToDec('17')}")
    print(f"Octal 17 -> Binary: {sb.octToBin('17')}")
    print(f"Octal 17 -> Hex: {sb.octToHex('17')}")
    print(f"Hex 1F -> Decimal: {sb.hexToDec('1F')}")
    print(f"Hex 1F -> Binary: {sb.hexToBin('1F')}")
    print(f"Hex 1F -> Octal: {sb.hexToOct('1F')}")


if __name__ == '__main__':
    # When run directly, show a small interactive menu.
    try:
        while True:
            print('\nSistem Bilangan - Pilih konversi:')
            print('1) Biner -> Desimal')
            print('2) Biner -> Hexadesimal')
            print('3) Oktal -> Desimal')
            print('4) Oktal -> Biner')
            print('5) Oktal -> Hexadesimal')
            print('6) Hex -> Desimal')
            print('7) Hex -> Biner')
            print('8) Hex -> Oktal')
            print('9) Tampilkan demo contoh')
            print('0) Keluar')
            choice = input('Pilihan: ').strip()
            if choice == '0':
                break
            if choice == '1':
                v = input('Masukkan bilangan biner: ')
                print('Desimal ->', sb.binToDec(v))
            elif choice == '2':
                v = input('Masukkan bilangan biner: ')
                print('Hexadesimal ->', sb.binToHex(v))
            elif choice == '3':
                v = input('Masukkan bilangan oktal: ')
                print('Desimal ->', sb.octToDec(v))
            elif choice == '4':
                v = input('Masukkan bilangan oktal: ')
                print('Biner ->', sb.octToBin(v))
            elif choice == '5':
                v = input('Masukkan bilangan oktal: ')
                print('Hexadesimal ->', sb.octToHex(v))
            elif choice == '6':
                v = input('Masukkan bilangan hex (contoh 1F): ')
                print('Desimal ->', sb.hexToDec(v))
            elif choice == '7':
                v = input('Masukkan bilangan hex: ')
                print('Biner ->', sb.hexToBin(v))
            elif choice == '8':
                v = input('Masukkan bilangan hex: ')
                print('Oktal ->', sb.hexToOct(v))
            elif choice == '9':
                _demo()
            else:
                print('Pilihan tidak dikenal, coba lagi.')
    except (KeyboardInterrupt, EOFError):
        print('\nKeluar')

