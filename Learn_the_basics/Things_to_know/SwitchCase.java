public class Solution {
    public static double areaSwitchCase(int ch, double []a) {
        // Write your code here
        double area=0;
        if(ch ==1){
            //using Math.PI was crutial since i had used decimal values it had some error
            area=Math.PI*a[0]*a[0];
            return area;
        }
        else if(ch==2){
            area=a[0]*a[1];
            return area;
        }
        return area;
    }
}

/*
PYTHON IMPLEMENTATION

from typing import *
import math
def areaSwitchCase(ch: int, a: List[float]):
    #match only supported after python 3.10
    # match ch:
    #     case 1:
    #         return (22/7)*a[0]*a[0]
    #     case 2:
    #         return a[0]*a[1]
    if ch == 1:
        ans=math.pi*a[0]*a[0]
        return ans
    elif ch == 2:
        ans=a[0]*a[1]
        return ans
*/
