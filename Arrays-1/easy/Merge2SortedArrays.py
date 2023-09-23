def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    a_p=0
    b_p=0
    temp=[]
    while a_p<len(a) and b_p<len(b):
        if a_p<len(a) and a[a_p]<=b[b_p]:
            temp.append(a[a_p])
            item=a[a_p]
            while a_p<len(a) and a[a_p]==item:
                a_p+=1
            while b_p<len(b) and b[b_p]==item:
                b_p+=1
        elif b_p<len(b) and b[b_p]<=a[a_p]:
            temp.append(b[b_p])
            item=b[b_p]
            while a_p<len(a) and a[a_p]==item:
                a_p+=1
            while b_p<len(b) and b[b_p]==item:
                b_p+=1
    # print(temp)
    item=temp[-1]
    if a_p==len(a):
        # temp+=b[b_p:]
        while b_p<len(b):
            if item==b[b_p]:
                b_p+=1
            else:
                temp.append(b[b_p])
                item=b[b_p]
                b_p+=1
    else:
        while a_p<len(a):
            if item==a[a_p]:
                a_p+=1
            else:
                temp.append(a[a_p])
                item=a[a_p]
                a_p+=1
    return temp