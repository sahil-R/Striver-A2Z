for i in range(6):
    counter=0
    for j in range(i):
        print(chr(ord("A")+counter),end="")
        counter+=1
    print("\n")