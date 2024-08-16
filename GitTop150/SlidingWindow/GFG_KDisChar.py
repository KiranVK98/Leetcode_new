import collections
class Solution:

    def longestKSubstr(self, s, k):
        # code here
        
        count = collections.defaultdict(int)
        
        left = 0
        
        longest = -1
        
        for right in range(len(s)):
            count[s[right]] += 1
            if(len(count) == k):
                longest = max(longest, right - left + 1)
                
            while(len(count) > k):
                count[s[left]] -= 1
                if(count[s[left]] == 0):
                    count.pop(s[left])
                left += 1


        return longest