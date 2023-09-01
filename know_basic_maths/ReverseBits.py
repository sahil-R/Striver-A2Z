def convert(n):
    b=[0]*32
    index=0
    while n:
        b[index]=n%2
        n//=2
        index+=1
    b=b[::-1]
    sum=0
    for i in range(32):
        sum+=(b[i])*2**i
    return sum



def reverseBits(n):
    b=convert(n)
    return b