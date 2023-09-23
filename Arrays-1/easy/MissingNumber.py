def missingNumber(a : List[int], N : int) -> int:
    # Write your code here.
    total=sum(a)
    n=N
    natural_sum=N*(N+1)//2
    return natural_sum-total

#Using XOR
    def missingNumber(self, nums: List[int]) -> int:
     xr1=0
     xr2=0
     for i in range(len(nums)):
         xr1^=nums[i]
         xr2^=(i+1)
         print(i)
     return xr1^xr2