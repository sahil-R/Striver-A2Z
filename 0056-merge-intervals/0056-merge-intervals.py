class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda a:a[0])

        start=-1
        end=-1
        ret=[]
        for interval in intervals:
            if not ret or interval[0]>ret[-1][1]:
                ret.append(interval)
            else:
                ret[-1][1]=max(ret[-1][1],interval[1])
        return ret