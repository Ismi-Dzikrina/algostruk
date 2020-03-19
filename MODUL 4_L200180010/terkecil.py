def cariterkecil(kumpulan):
    n = len(kumpulan)
    #anggap item pertama adalah yang terkecil
    terkecil = kumpulan[0]
    #tentukan apakah item lain lebih kecil
    for i in range(1,n):
        if kumpulan[i] < terkecil:
            terkecil = kumpulan[i]
    return terkecil #kembalikan yang terkecil
