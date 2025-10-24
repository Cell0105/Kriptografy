import tkinter as tk
from tkinter import messagebox

def hitung_nilai_akhir(sikap, tugas, uts, uas):
    total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)
    return total

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


root = tk.Tk()
root.title("Program Hitung Nilai Akhir Akademik")


tk.Label(root, text="Nilai Sikap/Kehadiran (0-100):").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_sikap = tk.Entry(root)
entry_sikap.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nilai Tugas (0-100):").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_tugas = tk.Entry(root)
entry_tugas.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Nilai UTS (0-100):").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_uts = tk.Entry(root)
entry_uts.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Nilai UAS (0-100):").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_uas = tk.Entry(root)
entry_uas.grid(row=3, column=1, padx=10, pady=5)


btn_hitung = tk.Button(root, text="Hitung", command=hitung)
btn_hitung.grid(row=4, column=0, columnspan=2, pady=10)


hasil_total = tk.Label(root, text="Total Nilai Akhir : -")
hasil_total.grid(row=5, column=0, columnspan=2, pady=2)

hasil_huruf = tk.Label(root, text="Nilai Huruf       : -")
hasil_huruf.grid(row=6, column=0, columnspan=2, pady=2)

hasil_bobot = tk.Label(root, text="Bobot             : -")
hasil_bobot.grid(row=7, column=0, columnspan=2, pady=2)

hasil_status = tk.Label(root, text="Keterangan        : -")
hasil_status.grid(row=8, column=0, columnspan=2, pady=2)

root.mainloop()
