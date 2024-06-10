class Solution:
    def recurse(self,nums,goal):
        left=0
        right=0
        count=0
        sum=0
        while right<len(nums):
            sum+=nums[right]
            # print(left,right,count,sum)
            while sum>goal and left<right:
                # print(left)
                sum-=nums[left]
                left+=1
            if sum<=goal:
                count+=(right-left+1)
            right+=1
        return count
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.recurse(nums,goal)-self.recurse(nums,goal-1)