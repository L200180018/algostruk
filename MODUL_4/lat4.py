c0 = 240000
c1 = 230000
c2 = 250000
c3 = 235000
c4 = 240000
c5 = 250000
c6 = 245000
c7 = 245000
c8 = 245000
c9 = 270000
c10 = 265000

daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]
def binSe(kumpulan,target):
    low=0
    high=len(kumpulan)-1
    while low <= high:
        mid=(high+low)//2
        if kumpulan[mid]==target:
            return True
        elif target < kumpulan[mid]:
            high=mid-1
        else:
            low=mid+1
    return False

print(binSe(daftar,245000))
print(binSe(daftar,270000))
