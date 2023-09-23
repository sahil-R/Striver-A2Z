def missingNumber(a : List[int], N : int) -> int:
    # Write your code here.
    total=sum(a)
    n=N
    natural_sum=N*(N+1)//2
    return natural_sum-total