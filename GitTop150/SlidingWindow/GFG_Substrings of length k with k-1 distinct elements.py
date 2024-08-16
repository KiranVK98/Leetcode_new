import collections
class Solution:
    def countOfSubstrings(self, S, K):
        # code here 
        left = 0
        result = 0
        
        count = collections.defaultdict(int)
        
        for right in range(len(S)):
            count[S[right]] += 1
            while(right - left + 1 > K or len(count) > K-1):
                count[S[left]] -= 1
                if(count[S[left]] == 0):
                    count.pop(S[left])
                    
                left += 1
                
                
            if(right - left + 1 == K and len(count) == K-1):
                result += 1
                
                
        return result