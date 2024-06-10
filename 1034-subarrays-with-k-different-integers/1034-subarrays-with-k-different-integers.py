class Solution:
    def solve(self,nums,k):
        map={}
        left=0
        right=0
        count=0
        while right<len(nums):
            # print(left,right,map)
            c=map.get(nums[right],0)
            if c==0:
                map[nums[right]]=1
            else:
                map[nums[right]]+=1
            while len(map)>k:
                map[nums[left]]-=1
                if map[nums[left]]==0:
                    map.pop(nums[left])
                left+=1
            if len(map)<=k:
                # print("here")
                temp=(right-left)+1
                # print(temp)
                count+=temp
            # print(count)
            right+=1
        return count            
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.solve(nums,k)-self.solve(nums,k-1)