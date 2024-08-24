class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for c in range(len(s)):
            if s[c] not in hash_map:
                hash_map[s[c]] = [c,1]
            else:
                hash_map[s[c]][1] = hash_map[s[c]][1] + 1



        ind = float('inf')
        for k,c in hash_map.items():
            # print(c)
            if(c[1] == 1):
                ind = min(ind,c[0])



        return -1 if ind == float('inf') else ind

