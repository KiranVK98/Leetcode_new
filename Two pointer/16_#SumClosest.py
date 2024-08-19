class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # -4 -1 1 2  

        nums.sort()

        sum = nums[0] + nums[1] + nums[2]

        for val in range(len(nums)):
            start = val + 1
            end = len(nums) - 1

            while(start < end):
                diff = (nums[val] + nums[start] + nums[end])
                if(diff < target):
                    start += 1

                else:
                    end -= 1


                if(abs(diff - target) < abs(sum - target)):
                    sum = diff


        return sum

                



        return sum