class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # letterDistinct = set()
        last_found = 0
        found = 0
        if(len(s) == 0):
            return True
        for key,letter in enumerate(s):

            for l in range(last_found,len(t)):
                if(letter == t[l]):
                    last_found = l+1
                    found += 1
                    # print(l,t[l])
                    if(found == len(s)):
                        return True
                    break
                
                


        return False