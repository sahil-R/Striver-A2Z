sum1=0
sum2=0

number=int(input())

while number>0:
    item=number%10
    if item%2==0:
        sum2+=item
    else:
        sum1+=item
    number//=10

print(sum2, " ", sum1)