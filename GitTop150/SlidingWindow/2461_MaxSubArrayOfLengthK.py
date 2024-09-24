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
'''
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0

        max_sum = 0

        sums = 0

        hash_set = set()
        for end in range(len(nums)):
            # print(start,end)
            while(len(hash_set) == k or nums[end] in hash_set):
                hash_set.remove(nums[start])
                sums -= nums[start]
                start += 1

            sums += nums[end]
            hash_set.add(nums[end])
            if(end - start + 1 == k):
                max_sum = max(max_sum,sums)

        return max_sum


'''

            

            