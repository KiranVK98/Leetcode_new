class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        result = ""
        for k,v in enumerate(strs):
            if k==0:
                result = v

            else:
                minimum = min(len(v), len(result))
                start = 0
                while(start<minimum):
                    if(v[start] != result[start]):
                        result = result[:start]
                        break
                    start +=1


        return result