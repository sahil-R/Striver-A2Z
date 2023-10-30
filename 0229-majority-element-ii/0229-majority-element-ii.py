class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_m1=0
        count_m2=0
        m1=0
        m2=0
        for i in nums:
            if count_m1==0 and i!=m2:
                count_m1=1
                m1=i
            elif count_m2==0 and i!=m1:
                count_m2+=1
                m2=i
            elif i==m1:
                count_m1+=1
            elif i==m2:
                count_m2+=1
            else:
                count_m1-=1
                count_m2-=1
        count_m1=0
        count_m2=0
        for i in nums:
            if i==m1:
                count_m1+=1
            elif i==m2:
                count_m2+=1
        mini=(len(nums)//3)+1
        if count_m1>=mini and count_m2>=mini:
            return [m1,m2]
        elif count_m1>=mini:
            return [m1]
        elif count_m2>=mini:
            return [m2]
        else:
            return []