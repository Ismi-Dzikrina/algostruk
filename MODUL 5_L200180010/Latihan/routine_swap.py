def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariposisiyangterkecil(A,darisini,sampaisini):
    posisiyangterkecil = darisini #anggap ini yang terkecil
    for i in range(darisini+ 1,sampaisini): #cari disisilist
        if A[i] < A[posisiyangterkecil]: #kalau menemukan yang lebih kecil,
            posisiyangterkecil = i   #anggapan dirubah
    return posisiyangterkecil





    
