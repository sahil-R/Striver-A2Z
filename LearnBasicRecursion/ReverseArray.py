from typing import *
def recurse(n,nums,li):
    if n<0:
        return li
    else:
        li.append(nums[n])
        return recurse(n-1,nums,li)

def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    return recurse(n-1,nums,[])