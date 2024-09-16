class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) 
        # ###
        # [7,3,2,4,8,2,3,1]
        #[]
        # ###
        while(start < end):
            if(nums[start] != start+1 and nums[start] != nums[nums[start]-1]):
                temp = nums[start]
                nums[start] = nums[nums[start]-1]
                nums[temp-1] = temp
                # print(nums)

            else:
                start += 1

        res = []
        for i in range(len(nums)):
            if(nums[i] != i+1):
                res.append(i+1)

        return res