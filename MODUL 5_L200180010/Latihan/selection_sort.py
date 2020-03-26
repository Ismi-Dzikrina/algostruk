from routine_swap import swap,cariposisiyangterkecil
def selectionsort(A):
    n = len(A)
    for i in range(n-1):
        indexkecil = cariposisiyangterkecil(A,i,n)
        if indexkecil != i:
            swap(A,i,indexkecil)
