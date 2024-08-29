class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sums = 0

        check = set()

        start = 0

        res = 0

        for end in range(len(nums)):
            while(nums[end] in check or end - start + 1 > k):
                sums -= nums[start]
                check.remove(nums[start])
                start += 1

            sums += nums[end]
            check.add(nums[end])

            if(end - start + 1 == k):
                res = max(res, sums)

        return res

            

            

            