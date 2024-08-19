class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #-2 -1 0 0 1 2

        res = []

        nums.sort()
        visited = set()
        for outer in range(len(nums)):
            for inner in range(outer + 1, len(nums)):
                start = inner + 1
                end = len(nums) - 1


                while(start < end):
                    cal = nums[outer] + nums[inner] + nums[start] + nums[end]

                    if(cal<target):
                        start += 1

                    elif(cal > target):
                        end -= 1

                    else:
                        ap = (nums[outer] , nums[inner] , nums[start] , nums[end])
                        if(ap not in visited):
                            res.append(ap)
                        start += 1
                        visited.add(ap)

        return res