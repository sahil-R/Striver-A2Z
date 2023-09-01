max=2
for i in range(max):
    for j in range(max-i):
        print("*",end="")
    for j in range(i):
        print(" ",end="")
    for j in range(i):
        print(" ",end="")
    for j in range(max-i,0,-1):
        print("*",end="")
    print("\n")
for i in range(max):
    for j in range(i+1):
        print("*",end="")
    for j in range(max-i-1):
        print(" ",end="")
    for j in range(max-i-1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print("*",end="")
    print("\n")