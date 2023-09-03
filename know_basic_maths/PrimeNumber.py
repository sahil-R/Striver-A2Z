from math import *
from collections import *
from sys import *
from os import *
n=int(input())
sum=1
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        sum+=1
if i!=1 and sum==2:
    print("YES")
else:
    print("NO")