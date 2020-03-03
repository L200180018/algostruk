def apakahKabisat(x):
    A = "kabisat"
    B = "Bukan kabisat"
    if x%4==0:
        if x%100==0 and x%400==0:
            return A
        elif x%100==0 and x%400!=0:
            return B
        return A
    return B
