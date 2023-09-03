from typing import List

def recurse(n,target,li):
    if n ==target:
        return li
    else:
         li.append(li[-1]+li[-2])
         return recurse(n+1,target,li)
def generateFibonacciNumbers(n: int) -> List[int]: 
    # Write your code here
    if n==1:
        return [n-1]
    return recurse(2,n,[0,1])