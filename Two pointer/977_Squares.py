class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)
        pt = len(nums) - 1
        while(left <= right):
            if(abs(nums[left]) <= abs(nums[right])):
                res[pt] = nums[right] * nums[right]
                right -= 1
            else:
                res[pt] = nums[left] * nums[left]
                left += 1

            pt -= 1

        return res