n=int(input())  
# taking n as a input 
## write your code !!
temp=str(n)
flag=False
for i in range(len(temp)//2):
    if temp[i]!=temp[len(temp)-1-i]:
        flag=True

if flag:
    print("false")
else:
    print("true")