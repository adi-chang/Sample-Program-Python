# soal:
# Buatlah script program python untuk mencari nilai FPB (Faktor Persekutuan Terbesar) dari dua buah bilangan int yang diinput oleh user 
# (nilai bilangan diinput bebas oleh user saat program running). 
# Lengkapi program anda dengan exception handling untuk menangani semua kemungkinan exception saat runtime yang bisa terjadi.

# solusi:
import os 


while True:
    os.system('cls')
    try:
        val_1 = int(input('Bilangan - 1 ? '))
        val_2 = int(input('Bilangan - 2 ? '))
    except Exception as e:
        print(f'\nError: {e}\n')
    else:
        a = val_1
        b = val_2
        while True:
            if a == b:
                break
            elif a > b:
                while True:
                    a -= 1
                    if val_1 % a == 0:
                        break
            else:
                while True:
                    b -= 1
                    if val_2 % b == 0:
                        break
        print(f'\n>>>FPB dari Bilangan {val_1} dan {val_2} adalah {a}\n')                    
    while True:
        ulang = input('Ulangi [y/n] ? ').lower()
        if ulang in ('y', 'n'):
            break
    if ulang == 'n':
        os.system('cls')
        break    
