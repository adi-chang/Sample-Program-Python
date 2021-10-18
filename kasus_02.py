# soal:
# Buatlah script program python untuk mencari nilai KPK (Kelipatan Persekutuan Terkecil) dari dua buah bilangan int yang diinput oleh user 
# (nilai bilangan diinput bebas oleh user saat program running). 
# Lengkapi program anda dengan exception handling untuk menangani semua kemungkinan exception saat runtime yang bisa terjadi. 
# Dalam aritmetika dan teori bilangan, kelipatan persekutuan terkecil (KPK) dari dua bilangan adalah 
# bilangan bulat positif terkecil yang dapat dibagi habis oleh kedua bilangan itu

# solusi:
import os


while True:
    os.system('cls')
    try:
        val_1 = int(input('bilangan - 1 ? '))        
        val_2 = int(input('bilangan - 2 ? '))        
        if val_1 == 0 or val_2 == 0:
            raise Exception('Nilai Bilangan - 1 dan Bilangan - 2 tidak boleh bernilai 0 (nol) ...')
    except Exception as e:
        print(f'\nError: {e}\n')
    else:
        a = val_1
        b = val_2
        while True:
            if a == b:
                break
            elif a < b:
                a += val_1
            else:
                b += val_2
        print(f'\n>>> KPK dari Bilangan {val_1} dan {val_2} adalah {a}\n')
    while True:
        ulang = input('Ulangi [y/n] ? ').lower()
        if ulang in ('y', 'n'):
            break
    if ulang == 'n':
        os.system('cls')
        break
    