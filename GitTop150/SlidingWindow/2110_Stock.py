class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        left = 0

        res = 1


        for right in range(1,len(prices)):

            while(left < right and prices[right]!=prices[right-1] - 1):
                left += 1


            res += right - left + 1


        return res


            