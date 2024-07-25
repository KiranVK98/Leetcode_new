class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls_s = s.split(" ")
        if(len(pattern) != len(ls_s)):
            return False
        # print(ls_s)
        visited = set()
        hash_check = {}
        for word in range(len(pattern)):
            if(pattern[word] not in hash_check):
                if(ls_s[word] in visited):
                    return False
                hash_check[pattern[word]] = ls_s[word]
                visited.add(ls_s[word])
            else:
                if(hash_check[pattern[word]] != ls_s[word]):
                    return False

        return True
