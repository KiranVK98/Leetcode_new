class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_element = set()
        for num in nums1:
            unique_element.add(num)

        result = []
        check = set()
        for num in nums2:
            if num not in check and num in unique_element:
                result.append(num)
                check.add(num)

        return result