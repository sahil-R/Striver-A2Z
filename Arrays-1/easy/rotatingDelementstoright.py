class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #left rotate code
        # temp=[]
        # for i in range(k):
        #     temp.append(arr[i])
        # for i in range(k,len(arr)):
        #     arr[i-k]=arr[i]
        # for i in range(k):
        #     arr[len(arr)-k+i]=temp[i]
        #right rotate code 
        temp=[]
        k=k%len(arr)
#for k == len(arr) the array becomes equal to the original array so modding it to make it the least rotations,then copying the first k elements in a temporay array,then i know that i have to move n-k elements,so did that while adjusting the indexes and then finally copied the out of 
        for i in range(len(arr)-k,len(arr)):
            temp.append(arr[i])
        for j in range(len(arr)-k):
            arr[len(arr)-1-j]=arr[len(arr)-1-j-k]
        print(temp,arr)
        for i in range(len(temp)):
            arr[i]=temp[i]
        print(arr)

class Solution:
    def reverse(self,left,right,arr):
        while left <= right:
            temp=arr[left]
            arr[left]=arr[right]
            arr[right]=temp
            left+=1
            right-=1

    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #left rotate code
        # temp=[]
        # for i in range(k):
        #     temp.append(arr[i])
        # for i in range(k,len(arr)):
        #     arr[i-k]=arr[i]
        # for i in range(k):
        #     arr[len(arr)-k+i]=temp[i]
        #right rotate code 
#         temp=[]
#         k=k%len(arr)
# #for k == len(arr) the array becomes equal to the original array so modding it to make it the least rotations,then copying the first k elements in a temporay array,then i know that i have to move n-k elements,so did that while adjusting the indexes and then finally copied the out of 
#         for i in range(len(arr)-k,len(arr)):
#             temp.append(arr[i])
#         for j in range(len(arr)-k):
#             arr[len(arr)-1-j]=arr[len(arr)-1-j-k]
#         print(temp,arr)
#         for i in range(len(temp)):
#             arr[i]=temp[i]
#         print(arr)
#mistake that this is done onlyfor left rotations i.e when we are rotating left then the left k elements should be rotated then the right n-k elements should be rotated and finall the whole array ,in case of right rotation the right k elements should be rotated then the left n-k elements should be rotated then the whole array
        n=len(arr)
        k=k%n
        self.reverse(0,n-k-1,arr)
        print(arr)
        self.reverse(n-k,len(arr)-1,arr)
        print(arr)
        self.reverse(0,len(arr)-1,arr)
        print(arr)