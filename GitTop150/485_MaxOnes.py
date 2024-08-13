class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0

        end = 0

        max_ones = 0



        while(end < len(nums)):
            if(nums[end] == 1):
                max_ones = max(max_ones , end - left + 1)
                end += 1

            else:
                while(end<len(nums) and nums[end] != 1):
                    end += 1
                    left = end


        return max_ones