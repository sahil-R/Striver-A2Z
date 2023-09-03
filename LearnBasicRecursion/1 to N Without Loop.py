from typing import List
def recurse(i,x,l):
    if i==x:
        l.append(i)
        return l
    else:
        l.append(i)
        return recurse(i+1,x,l)
def printNos(x: int) -> List[int]: 
    # Write your code here
    return recurse(1,x,[])