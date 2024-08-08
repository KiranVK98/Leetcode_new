class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        minimum_length = float('inf')

        for right in range(len(nums)):
            sum += nums[right]
            while(sum >= target):
                minimum_length = min(right-left+1, minimum_length)
                sum -= nums[left]
                left+=1

        return minimum_length if minimum_length != float('inf') else 0

            


