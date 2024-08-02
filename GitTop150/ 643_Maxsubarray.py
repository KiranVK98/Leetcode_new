class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        end = 0
        sum = 0
        result = float('-inf')
        while(end < len(nums)):
            while(end - start < k):
                sum += nums[end]
                end += 1

            avg = sum / k
            result = max(result, avg)
            sum -= nums[start]
            start += 1

        return result


            