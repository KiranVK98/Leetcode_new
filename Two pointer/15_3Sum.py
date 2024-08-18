class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        #-4 -1 -1 0 1 2

        nums.sort()
        for number in range(len(nums)):
            if(number > 0 and nums[number] == nums[number-1]):
                continue
            start = number + 1
            end = len(nums) - 1
            # print(number,start,end)
            while(start < end):
                if(nums[number] + nums[start] + nums[end] > 0):
                    end -= 1

                elif(nums[number] + nums[start] + nums[end] < 0):
                    start += 1
                else:
                    res.append([nums[number] , nums[start] , nums[end]])
                    start += 1
                    end -= 1
                    while(start < len(nums) and nums[start-1] == nums[start]):
                        start += 1


        return res