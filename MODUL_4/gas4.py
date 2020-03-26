from lat2 import *

def cariKurang(daftar):
    for i in daftar:
        if i.uangsaku < 250000:
            print(i)

cariKurang(daftar)
