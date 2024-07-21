class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        #Two pointer Solutiion
        while(i < len(s) and j < len(t)):
            if(s[i] == t[j]):
                i += 1
                j += 1

            else:
                j += 1

    
        return True if i == len(s) else False




        # letterDistinct = set()
        # last_found = 0
        # found = 0
        # if(len(s) == 0):
        #     return True
        # for key,letter in enumerate(s):

        #     for l in range(last_found,len(t)):
        #         if(letter == t[l]):
        #             last_found = l+1
        #             found += 1
        #             # print(l,t[l])
        #             if(found == len(s)):
        #                 return True
        #             break
                
                


        return False