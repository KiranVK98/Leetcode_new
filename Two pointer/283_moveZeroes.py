class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0

        while(left < len(nums) and right < len(nums)):
            if(nums[left] != 0):
                left += 1
            elif(right>left and nums[right] != 0):
                nums[left] , nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1


        # new_arr = []
        # no_zero = 0
        # for i in nums:
        #     if(i!=0):
        #         new_arr.append(i)
        #     else:
        #         no_zero+=1

        # start = 0
        # end = len(new_arr)

        # while(start<end):
        #     nums[start] = new_arr[start]
        #     start+=1

        # while(start < len(nums)):
        #     nums[start] = 0
        #     start+=1

            
      
           

                

        