def apakahKabisat(n):
    if n%4==0:
        if n%100==0 and n%400==0:
            return True
        elif n%100==0 and n%400!=0:
            return False
        return True
    return False

print(apakahKabisat(1851))
print(apakahKabisat(1900))
print(apakahKabisat(2000))
print(apakahKabisat(2400))
