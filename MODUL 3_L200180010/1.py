a = [[2,4],
     [6,21]]
b = [[2,67],
     [2,9],
     [1,5,"b",9]]
c = [[3,5,7],[21,87,9]]
d = [[1,2,3],[21,90,3],[6,5,78]]
e = [[1,2],[43,7]]
##Memastikan isi dan ukuran matrixnya konsisten
def cekkonsisten(n):
    x = len(n[0])
    z = 0
    for i in range(len(n)):
        if (len(n[i]) == x):
            z += 1
    if (z == len(n)):
        print("Matrix konsisten")
    else:
        print("Matrix tidak konsisten")

print("NOMOR 1A")
cekkonsisten(a)
cekkonsisten(b)
cekkonsisten(c)
cekkonsisten(d)
def cekinteger(n):
    x = 0
    y = 0
    for i in n:
        for j in i:
            y += 1
            if(str(j).isdigit() == False):
                print("Tidak semua isi matrix angka")
                break
            else:
                x += 1
    if (x == y):
        print("Semua isi matrix adalah angka")
cekinteger(a)
cekinteger(b)
##Mengambil ukuran matrix
def cekordo(n):
    x,y = 0,0
    for i in range(len(n)):
        x += 1
        y = len(n[i])
    print("Mempunyai ordo" + str(x) + "x" + str(y))
        
print("NOMOR 1B")
cekordo(a)
cekordo(b)
cekordo(c)
cekordo(d)
##Menjumlahkan 2 matrix
def jumlah(n,m):
    x,y = 0,0
    for i in range(len(n)):
        x += 1
        y = len(n[i])
    xy = [[0 for j in range(x)] for i in range(y)]
    
    z = 0
    if(len(n)==len(m)):
        for i in range(len(n)):
            if(len(n[i]) == len(m[i])):
                z+=1
    if(z==len(n) and z==len(m)):
        print("ukuran sama")
        for i in range(len(n)):
            for j in range(len(n[i])):
                xy[i][j] = n[i][j] + m[i][j]
        print(xy)
    else:
        print("ukuran beda")

print("NOMOR 1C")
jumlah(a,b)
jumlah(a,e)
##Mengkalikan 2 matrix
def kali(n,m):
    aa = 0
    x,y = 0,0
    for i in range(len(n)):
        x+=1
        y = len(n[i])
    v,w = 0,0
    for i in range(len(m)):
        v+=1
        w = len(m[i])
        
    if(y==v):
        print("bisa dikalikan")
        vwxy = [[0 for j in range(w)] for i in range(x)]
        for i in range(len(n)):
            for j in range(len(m[0])):
                for k in range(len(m)):
                    #print(n[i][k], m[k][j])
                    vwxy[i][j] += n[i][k] * m[k][j]
        print(vwxy)
            
    else:
        print("tidak memenuhi syarat")
print("NOMOR 1D")
kali(a,e)
kali(b,d)
##Menghitung determinan
def determinan(A, total=0):
    x = len(A[0])
    z = 0
    for i in range(len(A)):
        if (len(A[i]) == x):
           z+=1
    if(z == len(A)):
        if(x==len(A)):
            indices = list(range(len(A)))
            if len(A) == 2 and len(A[0]) == 2:
                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
                return val
            for fc in indices: 
                As = A 
                As = As[1:] 
                height = len(As) 
                for i in range(height): 
                    As[i] = As[i][0:fc] + As[i][fc+1:] 
                sign = (-1) ** (fc % 2) 
                sub_det = determinanHitung(As)
                total += sign * A[0][fc] * sub_det
        else:
            return """tidak bisa dihitung determinannya,
                    karena bukan matrix bujursangkar"""
    else:
        return """tidak bisa dihitung determinannya,karena bukan matrix bujursangkar"""
    return total
print("NOMOR 1E")
print(determinan(a))
print(determinan(b))

