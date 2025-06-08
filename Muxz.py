import rarfile
import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
from threading import Thread

def log(msg):
    output_text.config(state='normal')
    output_text.insert(tk.END, msg + '\n')
    output_text.see(tk.END)
    output_text.config(state='disabled')

def start_bruteforce():
    rar_path = rar_entry.get()
    wordlist_path = wordlist_entry.get()

    if not os.path.exists(rar_path):
        messagebox.showerror("Error", "File RAR tidak ditemukan.")
        return
    if not os.path.exists(wordlist_path):
        messagebox.showerror("Error", "Wordlist tidak ditemukan.")
        return

    Thread(target=crack_rar, args=(rar_path, wordlist_path)).start()

def crack_rar(file_path, wordlist_path):
    log("[+] Membuka file RAR...")
    try:
        rf = rarfile.RarFile(file_path)
    except Exception as e:
        log(f"[!] Gagal membuka file RAR: {e}")
        return

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = f.read().splitlines()
    except Exception as e:
        log(f"[!] Gagal membaca wordlist: {e}")
        return

    log(f"[+] Mencoba {len(passwords)} password...\n")

    for i, pwd in enumerate(passwords, 1):
        try:
            rf.extractall(pwd=pwd.encode('utf-8'))
            log(f"[✅] Password ditemukan: {pwd}")
            messagebox.showinfo("Sukses", f"Password ditemukan: {pwd}")
            return
        except:
            log(f"[{i}] Salah: {pwd}")
            continue

    log("\n[✘] Password tidak ditemukan dalam wordlist.")
    messagebox.showwarning("Gagal", "Password tidak ditemukan.")

# === GUI SETUP ===
root = tk.Tk()
root.title("Rar Brute V1")
root.geometry("500x500")
root.resizable(False, False)

#Logo ASCII Header (Visual)
logo = tk.Label(root, text="MUXZ Community | by RSP457", font=("Courier", 16, "bold"), fg="red")
logo.pack(pady=15)

# Input Fields ===
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Label(frame, text="File RAR: ").grid(row=0, column=0, sticky="e")
rar_entry = tk.Entry(frame, width=50)
rar_entry.grid(row=0, column=1, padx=5)
tk.Button(frame, text="File", command=lambda: rar_entry.insert(0, filedialog.askopenfilename(filetypes=[("RAR files", "*.rar")]))).grid(row=0, column=2)

tk.Label(frame, text="Wordlist: ").grid(row=1, column=0, sticky="e")
wordlist_entry = tk.Entry(frame, width=50)
wordlist_entry.grid(row=1, column=1, padx=5)
tk.Button(frame, text="File", command=lambda: wordlist_entry.insert(0, filedialog.askopenfilename(filetypes=[("Text files", "*.txt")]))).grid(row=1, column=2)

# Start Button
tk.Button(root, text="Start", command=start_bruteforce, bg="red", fg="white", width=25).pack(pady=15)

#  Output Log
output_text = scrolledtext.ScrolledText(root, height=15, width=70, state='disabled', font=("Courier", 10))
output_text.pack(pady=5)

root.mainloop()
