max=4
for i in range(max):
    for j in range(i+1):
        print(j+1,end="")
    for j in range(max-i-1):
        print(" ",end="")
    for j in range(max-i-1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print(j+1,end="")
    print("\n")