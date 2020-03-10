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
