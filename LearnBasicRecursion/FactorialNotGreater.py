from typing import *
def recurse(i,current,n,fact):
    if current > n:
        return fact
    else:
        current*=i
        if current<=n:
            fact.append(current)
        return recurse(i+1,current,n,fact)
def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    return recurse(1,1,n,[])
