class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if(m==0 and n==1):
            nums1[0] = nums2[0]
        i = m + n - 1
        while(i>=0):
            if(n<=0 or m<=0):
                break
            if(nums1[m-1] > nums2[n-1]):
                nums1[i] = nums1[m-1]
                m-=1
            else:
                nums1[i] = nums2[n-1]
                n-=1
            i-=1

        while(i>=0 and m>0):
            nums1[i] = nums1[m-1]
            m-=1
            i-=1

        while(i>=0 and n>0):
            nums1[i] = nums2[n-1]
            n-=1
            i-=1