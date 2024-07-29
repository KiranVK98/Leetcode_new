class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #with division
        prod = 1
        exists = False
        count = 0
        for val in nums:
            if(val!=0):
                prod = prod * val
            else:
                exists = True
                count+=1

        # if(count == len(nums)):
        #     return [0] * len(nums)

        if(count > 1):
            prod = 0
        answer = []

        if(exists):
            for val in nums:
                if(val!=0):
                    answer.append(0)
                else:
                    answer.append(prod)

            return answer
        for val in nums:
            answer.append(int(prod/val))
     

        return answer