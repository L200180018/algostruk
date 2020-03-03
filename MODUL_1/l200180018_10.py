def selesaikanABC(a,b,c):
    D = b**2 - (4*a*c)
    if D>0:
        print ("Determinannya positif. Persamaan Dua akar real berbeda")
    elif D == 0:
        print ("Determinannya nol. Persamaan Hanya memiliki satu akar real")
    else:
        print ("Determinannya negatif. Persamaan Tidak memiliki akar real")
