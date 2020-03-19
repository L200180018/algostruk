#2a
def buatNol(m,n= None):
    if n == None:
        n=m
    print([[0 for j in range (m)] for i in range (n)])
buatNol(2,3)
buatNol(3)

#2b
def buatIdentitas(n):
    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])

buatIdentitas(4)
buatIdentitas(2)
