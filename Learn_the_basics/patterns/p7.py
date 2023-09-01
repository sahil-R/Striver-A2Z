j=1
max=5
for i in range(max):
    for temp in range(2*max-j,0,-1):
        print(" ",end="")
    for temp in range(j):
        print("* ",end="")
    j+=2
    print("\n")