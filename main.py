import requests
from colorama import Fore, init
import os

# Inisialisasi colorama
init(autoreset=True)

def clear_terminal():
    # Membersihkan terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = r"""
███████╗██╗  ██╗███████╗██████╗  █████╗ ███╗   ██╗ ██████╗
██╔════╝██║  ██║██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔════╝
███████╗███████║█████╗  ██████╔╝███████║██╔██╗ ██║██║  ███╗
╚════██║██╔══██║██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██║   ██║
███████║██║  ██║███████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝
╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝
    """
    print(Fore.GREEN + banner)

    # Tampilkan teks di tengah terminal
    terminal_width = os.get_terminal_size().columns
    text = "SHerang Exploiter Crew"
    centered_text = text.center(terminal_width)
    print(Fore.GREEN + centered_text)

    # Informasi tambahan
    print(Fore.GREEN + "Admin  :", end=' ')
    print(Fore.WHITE + "03xploit")
    print(Fore.GREEN + "Tools  :", end=' ')
    print(Fore.WHITE + "Env Scanner")
    print(Fore.GREEN + "Github :", end=' ')
    print(Fore.WHITE + "github.com/sherangxcrew")
    print(Fore.GREEN + "Website:", end=' ')
    print(Fore.WHITE + "https://sherangxcrew.com")
    print("")
    print(Fore.LIGHTBLUE_EX + "Ketik exit untuk keluar")

def check_env_file(url):
    # Tambahkan /.env ke URL
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url  # Menambahkan http jika tidak ada

    env_url = url.rstrip('/') + '/.env'

    try:
        response = requests.get(env_url)
        if response.status_code == 200:
            print(Fore.GREEN + f"{env_url} (Found)")
            return env_url  # Kembalikan URL yang ditemukan
        elif response.status_code == 404:
            print(Fore.YELLOW + f"{env_url} (Not Found)")
        elif response.status_code == 403:
            print(Fore.RED + f"{env_url} (Forbidden)")
        else:
            print(Fore.LIGHTWHITE_EX + f"{env_url} (Unknown Status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error checking {env_url}: {e}")

    return None  # Kembalikan None jika tidak ditemukan

def main():
    clear_terminal()
    print_banner()

    while True:
        # Minta pengguna untuk memasukkan nama file
        filename = input(Fore.WHITE + "Masukkan nama file : ")

        if filename.lower() == 'exit':
            print(Fore.GREEN + "Keluar dari program.")
            return  # Keluar dari fungsi main

        # Membaca URL dari file
        try:
            with open(filename, 'r') as file:
                urls = file.readlines()
            break  # Keluar dari loop jika file berhasil dibaca
        except FileNotFoundError:
            print(Fore.RED + f"File {filename} tidak ditemukan. Silakan coba lagi.")

    good_urls = []

    for url in urls:
        url = url.strip()  # Menghapus spasi di awal dan akhir
        if url:  # Pastikan URL tidak kosong
            found_url = check_env_file(url)
            if found_url:
                good_urls.append(found_url)

    # Simpan hasil yang ditemukan
    if good_urls:                                                                                                             good_filename = f"good_{filename}"
        with open(good_filename, 'w') as good_file:
            for good_url in good_urls:
                good_file.write(good_url + '\n')
        print(Fore.GREEN + f"Hasil disimpan di {good_filename}")
    else:
        print(Fore.YELLOW + "Tidak ada URL yang ditemukan.")

if __name__ == "__main__":
    main(
