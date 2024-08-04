class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        end = 0
        sum = 0
        min_length = float('inf')
        while(end < len(nums)):
            sum += nums[end]
            while(sum >= target):
                min_length = min(min_length, end-start+1)
                sum -= nums[start]
                start += 1

            end+=1
            # print(sum, start, end) 

        return min_length if min_length!=float('inf') else 0