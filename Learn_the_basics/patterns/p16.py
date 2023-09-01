counter=0
for i in range(5):
    for j in range(i+1):
        print(chr(ord("A")+counter),end="")
    counter+=1
    print("\n")