for i in range(1,100):
    if(i % 3) == 0 and (i % 5) == 0 :
        i = "solo indah"
    elif(i % 3) == 0:
        i = "solo"
    elif(i % 5) == 0:
        i = "indah"
    print(i)
