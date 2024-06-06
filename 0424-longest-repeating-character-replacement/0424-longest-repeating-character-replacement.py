class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=[0]*26
        left=0
        right=0
        max_length=0
        while right<len(s):
            #print(left,right,s[left:right+1],max_length,max_length-max(count))
            item=s[right]
            count[ord(item)-ord("A")]+=1
            if (right-left+1)>=max_length and (right-left+1)-max(count)>k:
                count[ord(s[left])-ord("A")]-=1
                left+=1
            max_length=max(max_length,right-left+1)
            right+=1
        return max_length
