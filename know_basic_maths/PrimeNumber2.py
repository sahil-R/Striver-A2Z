from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
divisors=[0]*(n+1)
divisors[n]=1
for i in range(1,int(n**0.5)+1):
    square=i*i
    num=i
    if n%i==0:
        while(num<=square):
            divisors[num]=1
            num+=i
if sum(divisors)==2:
    print("YES")
else:
    print("NO")