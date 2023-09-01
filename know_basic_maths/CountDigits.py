def countDigits(n: int) -> int:
    dividend=n
    count=0
    while n>0:
        divisor=n%10
        if divisor!=0 and dividend%divisor==0:
            count+=1
        n//=10
    return count