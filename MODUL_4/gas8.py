from random import randint

def log2n(n):
    return 1 + log2n(n/2) if (n > 1) else 0

def quiz(angka):
    quiz = randint(1, angka)
    jawab = 0
    count = 1
    maks = log2n(angka)

    print('Saya menyimpan angka bulat antara 1 sampai {}. anda punya {}x kesempatan. coba tebak'.format(angka, maks))
    while jawab != quiz and count <= maks:
        jawab = int(input('Masukkan tebakan ke-{}:>'.format(count)))
        if jawab == quiz:
            print('Ya. Anda benar')
        elif jawab < quiz:
            print('Itu terlalu kecil. Coba lagi')
        else:
            print('Itu terlalu besar. Coba lagi')
        count += 1

quiz(10000)
