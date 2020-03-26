from lat2 import *

def cariTerkecil(daftar):
    terkecil = daftar[0].uangsaku
    for i in daftar:
        if i.uangsaku < terkecil:
            terkecil = i.uangsaku
    return terkecil

print(cariTerkecil(daftar))

