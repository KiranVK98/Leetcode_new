class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 0

        while(start < len(nums)):
            if(nums[start] != start+1):
                if(nums[nums[start]-1] == nums[start]):
                    return nums[start]
                else:
                    temp = nums[start]
                    nums[start] = nums[nums[start]-1]
                    nums[temp-1] = temp
            else:
                start += 1

#Did it without using Floyd Algorithm hence had to modify the array