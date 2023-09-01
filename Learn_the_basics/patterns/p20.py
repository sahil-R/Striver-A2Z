max=12
for i in range(max+1):
    half=max//2
    if i<max//2:
        for j in range(i+1):
            print("*",end="")
        for j in range(2*(half-i)):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
    else:
        for j in range(max-i+1):
            print("*",end="")
        for j in range(2*(i-half)):
            print(" ",end="")
        for j in range(max-i+1):
            print("*",end="")
    print("\n")