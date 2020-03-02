from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if n%1 ==0: #Jika nanti hasilnya bukan prima
                return False
                break
            else: #Jika nanti hasilnya prima
                return True

print(apakahPrima(112))
print(apakahPrima(57))
print(apakahPrima(25))
            
