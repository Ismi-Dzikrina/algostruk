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

class sembarangkelas(object):
    def metodesatu(self):
        pass
    def metodesembilan(self,stringbaru):
        pass
    
class Manusia(object):
    """kelas 'manusia' dengan inisiasi 'nama' """
    keadaan = 'lapar'
    def __init__(self,nama):
        self.nama = nama
    def ucapkansalam(self):
        print ("salam, namaku",self.nama)
    def makan(self,s):
        print("saya baru saja makan",s)
        self.keadaan = "kenyang"
    def olahraga (self,k):
        print("saya baru saja latihan",k)
        self.keadaan = 'lapar'
    def mengalikandengandua(self,n):
        return n*2

##p1 = Manusia("Fatimah")
##p1.ucapkansalam()

class Mahasiswa(Manusia):
    """class mahasiswa yang dibangun dari kelas manusia"""
    def __init__(self,nama,NIM,kota,us):
        """metode inisiasi ini menutupi metode inisiasi di kelas manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotatinggal =kota
        self.uangsaku = us
    def __str__(self):
        s = self.nama +",NIM"+ str(self.NIM)\
            +",tinggaldi" + self.kotatinggal \
            +", uangsaku Rp" + str(self.uangsaku) \
            +"tiap bulannya"
        return s
    def ambilnama (self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambiluangsaku(self):
        return self.uangsaku
    def makan(self,s):
        """metode ini menutupi metode 'makan' nya classs manusia.
        mahasiswa kalau makan sambil belajar."""
        print("saya baru saja makan", s,"sambil belajar")
        self.keadaan = "kenyang"
        
m1 = Mahasiswa("Jamil",234,"surakarta",250000)
m2 = Mahasiswa("andi",365,"magelang",375000)
m3 = Mahasiswa ("Sri",676,"yogyakarta",240000)


class MhsTIF(Mahasiswa):
    """class MhsTIF yang dibangun dari class mahasiswa"""
    def katakanpy(self):
        print("python is cool")

