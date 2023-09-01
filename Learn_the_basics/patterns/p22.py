max =4
for i in range(2*max-1):
    for j in range(2*max-1):
        left=j
        right=2*max-1-j-1
        top=i
        bottom=2*max-1-i-1
        print(max-min(left,right,top,bottom),end="")
    print("\n")
