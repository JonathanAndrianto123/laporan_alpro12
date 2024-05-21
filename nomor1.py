# input n kategori
n = int(input('Masukkan jumlah kategori: '))
# siapkan dictionary kosong
data_aplikasi = {}
# input nama kategori dan aplikasi di dalamnya
for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
# siapkan list kosong untuk nama-nama aplikasi
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    # masukkan dalam dictionary
    data_aplikasi[nama_kategori] = aplikasi
# tampilkan dictionary data_aplikasi
print(data_aplikasi)
daftar_aplikasi_list = []
# ambil semua daftar aplikasi dari setiap kategori
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))
print(daftar_aplikasi_list)

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)) :
    hasil = hasil.intersection(daftar_aplikasi_list[i])
print(f"yang muncul disemuanya : {hasil}")

kamus_apk = dict()
for apk_set in daftar_aplikasi_list :
    for apk in apk_set :
        if apk not in kamus_apk :
            kamus_apk[apk] = 1
        elif apk in kamus_apk:
            kamus_apk[apk] += 1
hasil2 = set()
for key, value in kamus_apk.items() :
        if value == 1 :
            hasil2.add(key)
print(f"yang muncul hanya sekali : {hasil2}")

if n > 2 :
    hasil3 = set()
    for key, value in kamus_apk.items() :
        if value == 2 :
            hasil3.add(key)
    print(f"yang muncul tepat dua kali : {hasil3}")