class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0

        left = 0

        prod = 1
        for right in range(len(nums)):
            prod = prod * nums[right]
            while(left <= right and prod >= k):
                prod = prod // nums[left]
                left += 1

            # print(right)
            result += (right - left + 1)
            # print(right, result)


        return result
            

            



