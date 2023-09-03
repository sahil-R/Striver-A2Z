"""
Needs to be changed to java to use tree map as python doesnt support any such function atleast till now

"""
from typing import List
import math
def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    frequency={}
    for item in v:
        if item in frequency.keys():
            frequency[item]+=1
        else:
            frequency[item]=1
    high=-math.inf
    low=math.inf
    hitem=None
    litem=None
    # print(frequency.items())
    for key in sorted(frequency.keys()):
        value=frequency[key]
        if value<low:
            low=value
            litem=key
        if value>high:
            high=value
            hitem=key
    return [hitem,litem]