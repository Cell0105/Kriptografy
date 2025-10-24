import tkinter as tk
from tkinter import messagebox

# ------------------------------
# Latihan 1: Kalkulator otomatis
# ------------------------------
def latihan1():
    def hitung_otomatis():
        try:
            a = float(entry_a.get())
            b = float(entry_b.get())
            hasil_jumlah.config(text=f"Penjumlahan: {a + b}")
            hasil_kurang.config(text=f"Pengurangan: {a - b}")
            hasil_kali.config(text=f"Perkalian: {a * b}")
            hasil_bagi.config(text=f"Pembagian: {a / b if b != 0 else 'Error: ÷0'}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    win = tk.Toplevel(root)
    win.title("Latihan 1 - Kalkulator Otomatis")

    tk.Label(win, text="Angka 1:").grid(row=0, column=0, padx=5, pady=5)
    entry_a = tk.Entry(win)
    entry_a.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(win, text="Angka 2:").grid(row=1, column=0, padx=5, pady=5)
    entry_b = tk.Entry(win)
    entry_b.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(win, text="Hitung Semua", command=hitung_otomatis).grid(row=2, column=0, columnspan=2, pady=10)

    hasil_jumlah = tk.Label(win, text="Penjumlahan: -")
    hasil_jumlah.grid(row=3, column=0, columnspan=2)

    hasil_kurang = tk.Label(win, text="Pengurangan: -")
    hasil_kurang.grid(row=4, column=0, columnspan=2)

    hasil_kali = tk.Label(win, text="Perkalian: -")
    hasil_kali.grid(row=5, column=0, columnspan=2)

    hasil_bagi = tk.Label(win, text="Pembagian: -")
    hasil_bagi.grid(row=6, column=0, columnspan=2)

# ------------------------------
# Latihan 2: Kalkulator interaktif
# ------------------------------
def latihan2():
    def hitung():
        try:
            a = float(entry1.get())
            b = float(entry2.get())
            op = entry_op.get()

            if op == '+':
                hasil = a + b
            elif op == '-':
                hasil = a - b
            elif op == '*':
                hasil = a * b
            elif op == '/':
                hasil = a / b if b != 0 else "Error: ÷0"
            else:
                hasil = "Operator tidak valid"

            label_hasil.config(text=f"Hasil: {hasil}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    win = tk.Toplevel(root)
    win.title("Latihan 2 - Kalkulator Interaktif")

    tk.Label(win, text="Angka 1:").grid(row=0, column=0, padx=5, pady=5)
    entry1 = tk.Entry(win)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(win, text="Angka 2:").grid(row=1, column=0, padx=5, pady=5)
    entry2 = tk.Entry(win)
    entry2.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(win, text="Operator (+, -, *, /):").grid(row=2, column=0, padx=5, pady=5)
    entry_op = tk.Entry(win)
    entry_op.grid(row=2, column=1, padx=5, pady=5)

    tk.Button(win, text="Hitung", command=hitung).grid(row=3, column=0, columnspan=2, pady=10)

    label_hasil = tk.Label(win, text="Hasil: -")
    label_hasil.grid(row=4, column=0, columnspan=2)

# ------------------------------
# Latihan 3: Hitung Nilai Akademik
# ------------------------------
def latihan3():
    def hitung_nilai_akhir(sikap, tugas, uts, uas):
        return (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

    def konversi_range(nilai):
        if 81 <= nilai <= 100:
            return "A", 4
        elif 76 <= nilai <= 80:
            return "B+", 3.5
        elif 71 <= nilai <= 75:
            return "B", 3
        elif 66 <= nilai <= 70:
            return "C+", 2.5
        elif 56 <= nilai <= 65:
            return "C", 2
        elif 46 <= nilai <= 55:
            return "D", 1
        else:
            return "E", 0

    def keterangan(nilai):
        return "Lulus" if nilai >= 56 else "Tidak Lulus"

    def hitung():
        try:
            sikap = float(entry_sikap.get())
            tugas = float(entry_tugas.get())
            uts = float(entry_uts.get())
            uas = float(entry_uas.get())

            total = hitung_nilai_akhir(sikap, tugas, uts, uas)
            huruf, bobot = konversi_range(total)
            status = keterangan(total)

            hasil_total.config(text=f"Total Nilai Akhir : {total:.2f}")
            hasil_huruf.config(text=f"Nilai Huruf       : {huruf}")
            hasil_bobot.config(text=f"Bobot             : {bobot}")
            hasil_status.config(text=f"Keterangan        : {status}")

        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid!")

    win = tk.Toplevel(root)
    win.title("Latihan 3 - Nilai Akademik")

    tk.Label(win, text="Nilai Sikap/Kehadiran (0-100):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entry_sikap = tk.Entry(win)
    entry_sikap.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(win, text="Nilai Tugas (0-100):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
    entry_tugas = tk.Entry(win)
    entry_tugas.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(win, text="Nilai UTS (0-100):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
    entry_uts = tk.Entry(win)
    entry_uts.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(win, text="Nilai UAS (0-100):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
    entry_uas = tk.Entry(win)
    entry_uas.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(win, text="Hitung", command=hitung).grid(row=4, column=0, columnspan=2, pady=10)

    hasil_total = tk.Label(win, text="Total Nilai Akhir : -")
    hasil_total.grid(row=5, column=0, columnspan=2, pady=2)

    hasil_huruf = tk.Label(win, text="Nilai Huruf       : -")
    hasil_huruf.grid(row=6, column=0, columnspan=2, pady=2)

    hasil_bobot = tk.Label(win, text="Bobot             : -")
    hasil_bobot.grid(row=7, column=0, columnspan=2, pady=2)

    hasil_status = tk.Label(win, text="Keterangan        : -")
    hasil_status.grid(row=8, column=0, columnspan=2, pady=2)

# ------------------------------
# Menu Utama
# ------------------------------
root = tk.Tk()
root.title("Menu Latihan")

tk.Label(root, text="Pilih Program Latihan:", font=("Arial", 12, "bold")).pack(pady=10)

tk.Button(root, text="Latihan 1: Kalkulator Otomatis", width=40, command=latihan1).pack(pady=5)
tk.Button(root, text="Latihan 2: Kalkulator Interaktif", width=40, command=latihan2).pack(pady=5)
tk.Button(root, text="Latihan 3: Nilai Akademik", width=40, command=latihan3).pack(pady=5)

root.mainloop()
