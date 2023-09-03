from typing import *

def countFrequency(n: int, m: int, edges: List[List[int]]):
    li=[0]*(n)
    for edge in edges:
        if edge<=n:
            li[edge-1]+=1
    return(li)