from typing import List

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    for i in range(len(arr)-1):
        pos=i+1
        minimum=arr[pos]
        j=pos
        while j<len(arr):
            if minimum>arr[j]:
                pos=j
                minimum=arr[j]
            j+=1
        if arr[i]>arr[pos]:
            temp=arr[i]
            arr[i]=arr[pos]
            arr[pos]=temp
        # print(arr)
    
