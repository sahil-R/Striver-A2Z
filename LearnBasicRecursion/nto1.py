from typing import List
def recurse(n,l):
    if n==0:
        return l
    else:
        l.append(n)
        return recurse(n-1,l)
def printNos(x: int) -> List[int]:
    # Write your code here
    return recurse(x,[])