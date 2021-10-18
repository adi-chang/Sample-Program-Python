# soal:
# Buatlah script program python yang dapat menerima input data berupa nim dan nama lengkap anda masing-masing. 
# Lengkapi program anda dengan exception handling untuk menangani semua kemungkinan exception saat runtime yang bisa terjadi. 
# Semua karakter pada nim harus berupa angka numeric. Timbulkan exception jika nim yang diinput user tidak memenuhi syarat.
# Program kemudian dapat melakukan hal-hal berikut ini:
# Menghitung banyak karakter pada data nim anda
# Menghitung banyak karakter angka ganjil
# Menghitung banyak karakter angka genap
# Menjumlahkan angka-angka pada data nim anda
# Menghitung banyak karakter huruf (a-z) pada data nama anda, spasi tidak ikut dihitung.

# solusi:
try:
    # input
    nim = input('Nim  ? ')
    nama = input('Nama ? ')

    # validasi - nim harus berisi angka semua
    if not nim.isnumeric():
        raise Exception('Sorry, Nim Harus Berupa Angka Numeric Semua ... ')

except Exception as e:
    print(f'Error: {e}')

else:
    # Menghitung banyak karakter pada data nim anda
    panjang_nim = len(nim)

    # Menghitung banyak karakter angka ganjil
    # Menghitung banyak karakter angka genap
    # Menjumlahkan angka-angka pada data nim anda
    hitung_ganjil = 0
    hitung_genap = 0
    jumlah = 0
    for c in nim:
        n = int(c)
        if n % 2:
            # ganjil
            hitung_ganjil += 1
        else:
            hitung_genap += 1
        jumlah += n

    # Menghitung banyak karakter huruf (a-z) pada data nama anda, spasi tidak ikut dihitung
    panjang_nama = len(nama.replace(' ', ''))

    print('Hasil Analisa:')
    print(f'Banyak karakter pada nim anda               = {panjang_nim:3} karakter')
    print(f'Banyak karakter angka ganjil                = {hitung_ganjil:3} karakter')
    print(f'Banyak karakter angka genap                 = {hitung_genap:3} karakter')
    print(f'Jumlah dari keseluruhan angka pada nim anda = {jumlah:3}')
    print(f'Banyak karakter huruf pada nama anda        = {panjang_nama:3} karakter')