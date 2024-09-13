class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Cyclic Sort pattern - store the values at their indices and find the missing number

        start = 0

        while(start < len(nums)):
            number = nums[start]

            if(number < len(nums) and start!=nums[start]):
                nums[number], nums[start] = nums[start], nums[number]

            else:
                start += 1


        for i in range(len(nums)):
            if(nums[i] != i):
                return i

        return i+1