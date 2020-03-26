from lat2 import *

def cariIndex(daftar, target):
    index = []
    for i in range(len(daftar)):
        if daftar[i].kotatinggal == target:
            index.append(i)
    return index

print(cariIndex(daftar, 'Klaten'))
