class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new=[]
        p1=0
        p2=0
        while p1<m and p2<n:
            if nums1[p1]<=nums2[p2]:
                new.append(nums1[p1])
                p1+=1
            if nums1[p1]>nums2[p2]:
                new.append(nums2[p2])
                p2+=1
        
        while p1!=m:
            new.append(nums1[p1])
            p1+=1
        while p2!=n:
            new.append(nums2[p2])
            p2+=1
        
        for i in range(len(new)):
            nums1[i]=new[i]