def calcGDC(n:int, m: int) -> int:
    # Write your code here
    while n!=0 and m!=0 and m!=n:
        if n>m:
            n=n%m
        if m>n:
            m=m%n
    if m==0:
        return n
    if n==0:
        return m
    return n