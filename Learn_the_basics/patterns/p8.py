j=1
max=5
for i in range(max):
    for temp in range(j):
        print(" ",end="")
    for temp in range(0,2*max-j,1):
        print("* ",end="")
    j+=2
    print("\n")