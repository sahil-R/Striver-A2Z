#an armstrong number or order n where n is the length of the number ,is a number where when every digit of the number is raised to the power n and added equals
#to the origiinal nunber eg 371=3^3+7^3+1^3

from os import *
from sys import *
from collections import *
from math import *
n=int(input())
length=len(str(n))
sum=0
dup=n
while dup>0:
    digit=dup%10
    sum+=digit**length
    dup//=10

if sum==n:
    print("true")
else:
    print("false")