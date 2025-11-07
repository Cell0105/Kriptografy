import tkinter as tk
from tkinter import messagebox, filedialog

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper().replace(" ", "")
    
    def prepare_key(self, text):
        key_repeated = ""
        key_index = 0
        for char in text:
            if char.isalpha():
                key_repeated += self.key[key_index % len(self.key)]
                key_index += 1
            else:
                key_repeated += " "
        return key_repeated
    
    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        key_repeated = self.prepare_key(plaintext)
        ciphertext = ""
        details = "=== DETAIL PROSES ENKRIPSI ===\n"
        details += f"Plaintext: {plaintext}\n"
        details += f"Key (diulang): {key_repeated}\n"
        details += "Langkah-langkah:\n"
        for i, (p, k) in enumerate(zip(plaintext, key_repeated)):
            if p.isalpha():
                p_val = ord(p) - ord('A')
                k_val = ord(k) - ord('A')
                c_val = (p_val + k_val) % 26
                c = chr(c_val + ord('A'))
                ciphertext += c
                details += f"Posisi {i+1}: {p} (val={p_val}) + {k} (val={k_val}) = {c} (val={c_val})\n"
            else:
                ciphertext += p
                details += f"Posisi {i+1}: {p} (non-alfabet, tetap sama)\n"
        details += f"Ciphertext: {ciphertext}\n"
        return ciphertext, details
    
    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        key_repeated = self.prepare_key(ciphertext)
        plaintext = ""
        details = "=== DETAIL PROSES DEKRIPSI ===\n"
        details += f"Ciphertext: {ciphertext}\n"
        details += f"Key (diulang): {key_repeated}\n"
        details += "Langkah-langkah:\n"
        for i, (c, k) in enumerate(zip(ciphertext, key_repeated)):
            if c.isalpha():
                c_val = ord(c) - ord('A')
                k_val = ord(k) - ord('A')
                p_val = (c_val - k_val) % 26
                p = chr(p_val + ord('A'))
                plaintext += p
                details += f"Posisi {i+1}: {c} (val={c_val}) - {k} (val={k_val}) = {p} (val={p_val})\n"
            else:
                plaintext += c
                details += f"Posisi {i+1}: {c} (non-alfabet, tetap sama)\n"
        details += f"Plaintext: {plaintext}\n"
        return plaintext, details

class VigenereGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vigenere Cipher GUI - Dark Mode")
        self.root.geometry("600x500")
        self.root.configure(bg="#2e2e2e")  # Tema gelap
        
        # Label untuk Nama dan NPM (di atas tengah)
        tk.Label(root, text="Nama: Marcel Filemon Naibaho", bg="#2e2e2e", fg="white", font=("Arial", 12, "bold")).pack(anchor='center', pady=5)
        tk.Label(root, text="NPM: 230840026", bg="#2e2e2e", fg="white", font=("Arial", 12, "bold")).pack(anchor='center', pady=2)
        
        # Label dan Entry untuk Kunci
        tk.Label(root, text="Masukkan Kunci (hanya huruf alfabet, contoh: LEMON):", bg="#2e2e2e", fg="white").pack(pady=5)
        self.key_entry = tk.Entry(root, width=50, bg="#4e4e4e", fg="white", insertbackground="white")
        self.key_entry.pack(pady=5)
        
        # Label dan Entry untuk Teks Input
        tk.Label(root, text="Masukkan Teks (Plaintext untuk enkripsi atau Ciphertext untuk dekripsi):", bg="#2e2e2e", fg="white").pack(pady=5)
        self.text_entry = tk.Entry(root, width=50, bg="#4e4e4e", fg="white", insertbackground="white")
        self.text_entry.pack(pady=5)
        
        # Frame untuk tombol
        button_frame = tk.Frame(root, bg="#2e2e2e")
        button_frame.pack(pady=5)
        
        # Tombol untuk Enkripsi
        self.encrypt_button = tk.Button(button_frame, text="Enkripsi", command=self.encrypt, bg="#4CAF50", fg="white")
        self.encrypt_button.pack(side=tk.LEFT, padx=5)
        
        # Tombol untuk Dekripsi
        self.decrypt_button = tk.Button(button_frame, text="Dekripsi", command=self.decrypt, bg="#2196F3", fg="white")
        self.decrypt_button.pack(side=tk.LEFT, padx=5)
        
        # Tombol Save
        self.save_button = tk.Button(button_frame, text="Simpan Detail ke File", command=self.save_to_file, bg="#FF9800", fg="white")
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        # Area untuk Output Detail
        tk.Label(root, text="Detail Proses:", bg="#2e2e2e", fg="white").pack(pady=5)
        self.output_text = tk.Text(root, height=15, width=70, bg="#4e4e4e", fg="white", insertbackground="white")
        self.output_text.pack(pady=5)
        
        # Tombol Clear
        self.clear_button = tk.Button(root, text="Clear", command=self.clear, bg="#f44336", fg="white")
        self.clear_button.pack(pady=5)
    
    def encrypt(self):
        key = self.key_entry.get().strip()
        if not key.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Kunci harus berupa huruf alfabet saja!")
            return
        plaintext = self.text_entry.get().strip()
        if not plaintext:
            messagebox.showerror("Error", "Masukkan teks untuk dienkripsi!")
            return
        
        cipher = VigenereCipher(key)
        encrypted, details = cipher.encrypt(plaintext)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, details)
        
        # Verifikasi dengan dekripsi
        decrypted, _ = cipher.decrypt(encrypted)
        self.output_text.insert(tk.END, "\n" + "="*50 + "\n")
        self.output_text.insert(tk.END, f"Verifikasi: Plaintext asli == Decrypted? {plaintext.upper() == decrypted}\n")
    
    def decrypt(self):
        key = self.key_entry.get().strip()
        if not key.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Kunci harus berupa huruf alfabet saja!")
            return
        ciphertext = self.text_entry.get().strip()
        if not ciphertext:
            messagebox.showerror("Error", "Masukkan teks untuk didekripsi!")
            return
        
        cipher = VigenereCipher(key)
        decrypted, details = cipher.decrypt(ciphertext)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, details)
    
    def save_to_file(self):
        content = self.output_text.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "Tidak ada detail untuk disimpan!")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Sukses", f"Detail disimpan ke {file_path}")
    
    def clear(self):
        self.key_entry.delete(0, tk.END)
        self.text_entry.delete(0, tk.END)
        self.output_text.delete(1.0, tk.END)

# Jalankan GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereGUI(root)
    root.mainloop()
