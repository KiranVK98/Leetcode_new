class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = 0
        sum = 0
        result = float('-inf')

        for right in range(len(nums)):
            if(sum <= 0 and nums[right] >= 0):
                sum = nums[right]

            else:
                sum += nums[right]
            result = max(result, sum,nums[right])



        return 0 if result == float('-inf') else result