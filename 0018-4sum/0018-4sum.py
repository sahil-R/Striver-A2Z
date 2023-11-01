class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums=sorted(nums)
        ret=[]
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            while j<len(nums):
                # if j!=1 and nums[j]==nums[j-1]:
                #     continue
                k=j+1
                l=len(nums)-1
                while k<l:
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum>target:
                        l-=1
                    elif sum<target:
                        k+=1
                    else:
                        ret.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1
                j+=1
                while j<len(nums) and nums[j]==nums[j-1]:
                    j+=1
                
        return ret