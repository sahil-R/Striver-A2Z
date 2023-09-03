from  typing import *

def recurse(i,n,l):
    if i==n:
        return l
    else:
        l.append("Coding Ninjas")
        return recurse(i+1,n,l)
def printNtimes(n: int) -> None:
    l= recurse(0,n,[])
    print(" ".join(l))