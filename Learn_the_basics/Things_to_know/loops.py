from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
if n ==1:
    print(1)
elif n==2:
    print(1)
else:
    a=1
    b=1
    for i in range(2,n):
        next=a+b
        a=b
        b=next
    print(b)