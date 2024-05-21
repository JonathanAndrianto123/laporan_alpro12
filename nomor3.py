def teks_file(filename):
    try:
        with open(filename, 'r') as file:
            teks = file.read().lower()
            return set(teks.split())
    except FileNotFoundError:
        print(f"{filename}' tidak ditemukan")
        return set()

file1 = input("masukan nama file 1 :")
file2 = input("masukan nama file 2 :")
teks1 = teks_file(file1)
teks2 = teks_file(file2)

teks_sama = teks1 & teks2

if len(teks_sama) == 0 :
    print("tidak ada kata yang muncul pada kedua file")
else :
    print(f"kata-kata yang muncul di kedua teks adalah : {teks_sama}")