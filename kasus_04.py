import os
from array import *
from random import randint


os.system('cls')


try:
    n = int(input('banyak bilangan acak (2 - 10000) ? '))

    if n < 2 or n > 10_000:
        raise Exception('Sorry, n harus lebih besar dari 2 dan lebih kecil atau sama dengan 10000')

except Exception as e:
    print('Error:', e)

else:
    arr = array('i', [randint(1, 100) for _ in range(n)])

    # tampilkan isi arr
    print('\nData:')
    print('-----')
    c = 0
    for i in range(len(arr)):
        print(f'{arr[i]:3}', end=' ')
        c += 1
        if c % 30 == 0:
            print()
    print()

    # print jumlah
    if len(arr) % 30: print()
    print(f'jumlah dari keseluruhan elemen data = {sum(arr):,}\n')


