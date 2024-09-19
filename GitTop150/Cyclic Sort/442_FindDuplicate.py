class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        start = 0
        #[7,3,2,4,8,2,3,1]
        #[3,3,2,4,8,2,7,1]
        #[2,3,3,4,8,2,7,1]
        #[3,2,3,4,8,2,7,1]
        while(start < len(nums)):
            if(nums[start]!=-1 and start+1 != nums[start]):
                switchs = False
                # print(nums)
                if(nums[nums[start]-1] == nums[start]):
                    res.append(nums[start])
                    nums[nums[start]-1] = -1
                    start += 1
                    # print("EX")
                    continue

                # print("HAAA")
                temp = nums[start]
                nums[start] = nums[nums[start] - 1]
                nums[temp - 1] = temp

            else:
                start += 1


        return res