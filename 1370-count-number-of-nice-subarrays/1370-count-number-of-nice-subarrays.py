class Solution:
    def recurse(self,nums,k):
        left=0
        right=0
        odd=0
        count=0
        while right<len(nums):
            if nums[right]%2==1:
                odd+=1
            while odd>k:
                if nums[left]%2==1:
                    odd-=1
                left+=1
            if odd<=k:
                count+=right-left+1
            right+=1
        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.recurse(nums,k)-self.recurse(nums,k-1)