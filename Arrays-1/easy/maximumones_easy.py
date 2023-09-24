class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum=0
        temp=0
        for i in nums:
            # print(temp,maximum,i)
            if i==0:
                if temp>maximum:
                    maximum=temp
                    temp=0
                else:
                    temp=0
            else:
                temp+=1
        if temp>maximum:
            maximum=temp
        return maximum