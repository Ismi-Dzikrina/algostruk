from lat2 import mergeSort
from lat3 import quickSort
class Mahasiswa:
    keadaan = 'lapar'
    def __init__(self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.nim) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' perharinya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.nim
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print('Saya baru aja makan', s, 'sambil nugas')
        self.keadaan = 'kenyang'

mh1 = Mahasiswa("Andi", 14, "Sragen", 10000)
mh2 = Mahasiswa("Budi", 11, "Klaten", 13000)
mh3 = Mahasiswa("Rozaq", 26, "Boyolali", 12000)
mh4 = Mahasiswa("Putri", 37, "pekalongan", 12000)
mh5 = Mahasiswa("Billy", 24, "Bandung", 2000)

A = [mh1.nim, mh2.nim, mh3.nim, mh4.nim, mh5.nim]
mergeSort(A)
print(A)
