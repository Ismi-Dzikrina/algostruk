from time import time as detak
from random import shuffle as kocok
from lat2 import mergeSort
from lat3 import*

k = [i for i in range(1, 6000)]
kocok(k)

def swap(A, p, q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp
def cariposisiterkecil(A, darisini, sampaisini):
    posisiterkecil = darisini
    for i in range(darisini + 1, sampaisini):
        if A[1] < A[posisiterkecil]:
            posisiterkecil = 1
    return posisiterkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def selectionSort(A):
    n = len(A)
    for i in range(n - 1):
        indexkecil = cariposisiterkecil(A, i, n)
        if indexkecil != i:
            swap(A, i, indexkecil)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

bub = k[:]
sel = k[:]
ins = k[:]
mer = k[:]
qui = k[:]

aw = detak(); bubbleSort(bub); ak = detak(); print('bubble : %g detik' % (ak-aw))
aw = detak(); selectionSort(sel); ak = detak(); print('selection : %g detik' % (ak-aw))
aw = detak(); insertionSort(ins); ak = detak(); print('insertion : %g detik' % (ak-aw))
aw = detak(); mergeSort(mer); ak = detak(); print('merge : %g detik' % (ak-aw))
aw = detak(); quickSort(qui); ak = detak(); print('quick : %g detik' % (ak-aw))
