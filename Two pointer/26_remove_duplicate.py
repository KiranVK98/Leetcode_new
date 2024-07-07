class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        start = 1
        end = 1

        while(end < len(nums)):
            # print(start,end,nums)
            while(end < len(nums) and nums[end] == nums[end-1]):
                end += 1
            if(end >= len(nums)):
                break

            nums[start] = nums[end]
            start += 1
            end += 1
            
        # print(start,end,nums)
        return start
    

test = Solution()
print(test.removeDuplicates([1,1]))

print(test)