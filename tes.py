import os
import time
import shutil

# Banner keren
def banner():
    print(r"""
██    ██ ███████  ██████  ██     ██      ██████  ███    ██  ██████  ███████ ███████ 
██    ██ ██      ██    ██ ██     ██     ██    ██ ████   ██ ██       ██      ██      
██    ██ █████   ██    ██ ██  █  ██     ██    ██ ██ ██  ██ ██   ███ █████   ███████ 
██    ██ ██      ██    ██ ██ ███ ██     ██    ██ ██  ██ ██ ██    ██ ██           ██
 ██████  ███████  ██████   ███ ███       ██████  ██   ████  ██████  ███████ ███████ 
                                                                                   
""")

# Cek apakah Termux API tersedia
def cek_termux_api():
    if not shutil.which("termux-screencap") or not shutil.which("termux-screenrecord"):
        print("[!] Termux API belum tersedia atau belum terinstall.")
        print("=> Jalankan perintah: pkg install termux-api")
        exit()

# Fungsi rekam layar
def record_screen(duration=10):
    print("[*] Merekam layar selama", duration, "detik...")
    output_path = "/sdcard/Download/wa_viewonce_capture.mp4"
    os.system(f"termux-screenrecord -l {duration} {output_path}")
    print(f"[+] Video disimpan ke {output_path}")
    os.system(f"termux-media-scan {output_path}")
    os.system(f"termux-open {output_path}")

# Fungsi screenshot
def take_screenshot():
    timestamp = int(time.time())
    path = f"/sdcard/Download/wa_viewonce_{timestamp}.png"
    os.system(f"termux-screencap -p {path}")
    print(f"[+] Screenshot disimpan: {path}")
    os.system(f"termux-media-scan {path}")
    os.system(f"termux-open {path}")

# Menu utama
def menu():
    cek_termux_api()
    banner()
    while True:
        print("""
==== WA ViewOnce Capture ====
1. Screenshot (langsung)
2. Rekam layar (10 detik)
3. Keluar
""")
        choice = input("Pilih opsi: ")
        if choice == '1':
            take_screenshot()
        elif choice == '2':
            record_screen()
        elif choice == '3':
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid!")

# Jalankan program
if __name__ == "__main__":
    menu()
