#No 1
class MhsTIF(object):
   
    def __init__(self,nama,NIM,asal,saku):
        self.nama = nama
        self.NIM = NIM
        self.asal = asal
        self.saku = saku
        
c0 = MhsTIF ('Ika','L200180001','Sukoharjo', 240000)
c1 = MhsTIF ('Budi','L200180010','Sragen', 230000)
c2 = MhsTIF ('Ahmad','L200180002','Surakarta', 250000)
c3 = MhsTIF ('Chandra','L200180004','Surakarta', 230000)
c4 = MhsTIF ('Eka','L200180005','Boyolali', 240000)
c5 = MhsTIF ('Fandi','L20018006','Salatiga', 250000)
c6 = MhsTIF ('Deni','L200180007','Klaten', 245000)
c7 = MhsTIF ('Galuh','L20018008','Wonogiri', 245000)
c8 = MhsTIF ('Janto','L200180009','Klaten', 245000)
c9 = MhsTIF ('Hasan','L2001800011','Karanganyar', 270000)
c10 = MhsTIF ('Khalid','L200180012','Purwodadi', 265000)
Mhs = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def urutkan(A):
    baru = {}
    for i in range(len(A)):
        baru[A[i].nama] = A[i].NIM
    listofTuples = sorted(baru.items(), key = lambda x: x[1])
    for elemen in listofTuples :
        print(elemen[0], ":", elemen[1])
#print(urutkan(Mhs))


#No 2
def bubbleSort(arr):
    n = len(arr)
    for i in range (n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
def gabung(a,b):
    c = []
    c = a+b
    n = len(c)
    for i in range(n):
        for j in range(0, n-i-1):
            if c[j] > c[j+1] :
                c[j], c[j+1] = c[j+1], c[j]
    return c

a = [3,5,7,8,9,22,45,66]
b = [44,12,23,45,33,65,77]
a , b = bubbleSort(a),bubbleSort(b)
#print(gabung(a,b))

#No 3
from time import time as detak
from random import shuffle as kocok
k = [i for i in range(1,6001)]
kocok(k)
def u_bub(arr):
    n = len (arr)
    for i in range (n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
def u_sel(A):
    for i in range(len(A)):
        min_in = i
        for j in range(i+1, len (A)):
            if A[min_in] > A[j]:
                    min_in = j
        A[i], A[min_in] = A[min_in], A[i]
def u_ins(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

bub = k[:]
sel = k[:]
ins = k[:]

aw = detak(); u_bub(bub);ak = detak();print('bubble : %g detik' %(ak-aw));
aw1 = detak(); u_sel(sel);ak1 = detak();print('selection : %g detik' %(ak1-aw1));
aw2 = detak(); u_ins(ins);ak2 = detak();print('insertion : %g detik' %(ak1-aw1));
