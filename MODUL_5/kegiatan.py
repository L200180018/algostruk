def swap(A, p, q):
    tmp = A[p]
    A[p]= A[q]
    A[q]= tmp
    
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini               #->anggap ini yang terkecil
    for i in range(dariSini+1, sampaiSini):     #->cari disisa list
        if A[i] < A[posisiYangTerkecil]:        #->kalau menemukan yang lebih kecil
            posisiYangTerkecil = i              #->anggapan dirubah
    return posisiYangTerkecil
k = [50,20,70,10]
swap(k,1,3)
#print(k)

a = [40,10,40,20,90,60]
j = cariPosisiYangTerkecil(a,2,len(a))
#print(j)

#Latihan 5.1
def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
a = [40,10,40,20,90,60]
bubbleSort(a)
#print(a)

#Latihan 5.2
def selectionSort(a):
    n = len(a)
    for i in range(n-1):
        indexKecil=cariPosisiYangTerkecil(a,i,n)
        if indexKecil != i:
            swap(a,i,indexKecil)

b = [30,10,60,20,70,50]
selectionSort(b)
#print(b)

#Latihan 5.3
def insertionSort(a):
    n = len(a)
    for i in range(1,n):
        nilai = a[i]
        pos = i
        while pos > 0 and nilai < a[pos-1]:
            a[pos] = a[pos-1]
            pos = pos-1
        a[pos] = nilai

c = [20,10,90,30,70,50]
insertionSort(c)
print(c)
