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

        """Time complexity of O(n+d) and space complexity of O(d) since using a temporary array"""