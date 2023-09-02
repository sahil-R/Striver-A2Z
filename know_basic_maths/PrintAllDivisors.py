
def get_divisor_sum(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    return sum

def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    total=0
    for i in range(1,n+1):
        total+=get_divisor_sum(i)
    return total