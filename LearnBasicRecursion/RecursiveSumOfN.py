from typing import List

def recurse(n,sum):
    if n==0:
        return sum
    else:
        return recurse(n-1,sum+n)
def sumFirstN(n: int) -> int:
    # Write your code here.
    return recurse(n,0)