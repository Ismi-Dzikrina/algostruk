class Pesan(object):
    """sebuah class bernama pesan.
    untuk memahami kosep kelas dan object."""
    def __init__(self,sebuahstring):
        self.teks = sebuahstring
    def cetakini(self):
        print(self.teks)
    def cetakpakaihurufkapital(self):
        print(str.upper(self.teks))
    def cetakpakaihurufkecil(self):
        print(str.lower(self.teks))
    def jumkar(self):
        return len(self.teks)
    def cetakjumlahkarakter(self):
        print("kalimatku mempunyai ",len (self.teks),"karakter")
    def perbaruhi(self,stringbaru):
        self.teks = stringbaru
    def apakahterkandung(self):
        if (self == object):
            return True
        else:
            return False
    
