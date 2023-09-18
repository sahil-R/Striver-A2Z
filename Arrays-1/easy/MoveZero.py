class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # for i in range(n):
        #     if nums[i]==0:
        #         for j in range(i+1,n):
        #             if nums[j]!=0:
        #                 # print(i,j)
        #                 temp=nums[i]
        #                 nums[i]=nums[j]
        #                 nums[j]=temp
        #                 break
        # print(nums)


        
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         temp.append(nums[i])
        # # print(temp)
        # for j in range(len(nums)-len(temp)):
        #     temp.append(0)
        # print(temp)
        # for i in range(len(nums)):
        #     nums[i]=temp[i]
        
        #two pointer modification of the first approach is the optimal solution for this problem
        n=len(nums)
        j=None 
        for i in range(n):
            if nums[i]==0:
                j=i
                break
        if j!=None:
            for i in range(j+1,n):
                if nums[i]!=0:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
                    j+=1
                

