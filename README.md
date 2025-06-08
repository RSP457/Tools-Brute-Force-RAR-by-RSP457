# 🔐 Tools Brute Force RAR by MUXZ | RSP457

Alat sederhana untuk melakukan brute-force terhadap file `.rar` menggunakan wordlist. Dibuat untuk keperluan edukasi dan pengujian keamanan arsip.

```
███╗   ███╗██╗   ██╗██╗  ██╗███████╗
████╗ ████║██║   ██║██║ ██╔╝██╔════╝
██╔████╔██║██║   ██║█████╔╝ █████╗
██║╚██╔╝██║██║   ██║██╔═██╗ ██╔══╝
██║ ╚═╝ ██║╚██████╔╝██║  ██╗███████╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

MUXZ | by RSP457
```

---

## 🧰 Fitur

- Brute force password file `.rar`
- Support file wordlist `.txt`
- Versi CLI dan GUI tersedia
- Proses otomatis berhenti saat password ditemukan
- Support Windows (Python)

---

## 📥 Instalasi

1. git clone

```bash
git clone https://github.com/RSP457/Tools-Brute-Force-RAR-by-RSP457
```

2. masuk folder

```bash
cd Tools-Brute-Force-RAR-by-RSP457
```

3. Install dependensi:

```bash
pip install patool requirements.txt
```

4. Running

```bash
python3 Muxz.py
```

---

## 🚀 Penggunaan CLI

```bash
python MuxZ.py -f path/to/file.rar -w path/to/wordlist.txt
```

Contoh:

```bash
python MuxZ.py -f secret.rar -w wordlist.txt
```

---

## 💻 Penggunaan GUI

Jalankan file:

```bash
python MuxZ_GUI.py
```

Lalu pilih file `.rar` dan file `wordlist.txt` melalui tampilan antarmuka.

---

## 📝 Format Wordlist

Isi wordlist dalam file `.txt`, satu password per baris:

```
123456
password
qwerty
rarpass123
admin123
```

---

## ⚠️ Disclaimer

> Tools ini dibuat untuk **pembelajaran** dan **pengujian** keamanan. **Dilarang** digunakan untuk tujuan ilegal atau tanpa izin. Gunakan dengan tanggung jawab pribadi.

---

## 👨‍💻 Developer

**MUXZCommunity**  
🧑‍💻 by RSP457

---

## 📄 Lisensi

[MIT License](LICENSE)
