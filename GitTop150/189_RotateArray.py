class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #7654321
        def reverse_logic(start,end):
            while(start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        #reverse and reverse again twice - first k elements and post that
        k = k%len(nums)
        if(k!=0):
            nums.reverse()
            start = 0
            end = k-1
            reverse_logic(start,end)
            

            start = k
            end = len(nums)-1
            reverse_logic(start,end)

        