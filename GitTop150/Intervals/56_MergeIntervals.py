class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for interval in intervals:
            if not res:
                res.append(interval)

            else:

                if(interval[0] <= res[-1][1]):
                    res[-1][1] = max(interval[1], res[-1][1])

                else:
                    res.append(interval) #S


        return res