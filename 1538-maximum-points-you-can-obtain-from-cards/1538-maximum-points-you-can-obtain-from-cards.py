class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maximum=0
        leftsum=sum(cardPoints[:k])
        maximum=leftsum
        rightsum=0
        if k>len(cardPoints):
            return sum(cardPoints)
        for i in range(k):
            rightsum+=cardPoints[-i-1]
            leftsum-=cardPoints[k-i-1]
            maximum=max(maximum,leftsum+rightsum)
        print(leftsum,rightsum)
        maximum=max(maximum,rightsum)
        return maximum