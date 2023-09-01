max=4
for i in range(max+1):
    counter=0
    for j in range(max-i):
        print(" ",end="")
    for j in range(i):
        print(chr(ord("A")+counter),end="")
        counter+=1
    counter-=2
    for j in range(i-1):
        print(chr(ord("A")+counter),end="")
        counter-=1
    print("\n")