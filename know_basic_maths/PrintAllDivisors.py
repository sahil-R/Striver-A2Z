#This is done with optimal time complexity where we have an observation as follows
#for divisors of 36 we make an observation:
# 1*36=36
# 2*18=36
# 3*12=36
# 4*9=36
# 6*6=3
# ---------------
# 9*4=36
# 12*3=36
# 18*2=36
# 36*1=36
#Here if we make an observation that till 6 we have both n%i and n/i which divide the number completely
#after that it is just repeating the numbers
def get_divisor_sum(n):
    sum=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            sum+=i
            if i!=n//i:
                sum+=n//i
    return sum

def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    total=0
    for i in range(1,n+1):
        total+=get_divisor_sum(i)
    return total