class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        left = 0

        contains = collections.defaultdict(int)

        nice = 0
        for right in range(len(s)):
            contains[s[right]] += 1

            if(right - left + 1 == 3):
                if(len(contains) == 3):
                    nice += 1

                contains[s[left]] -= 1
                if(contains[s[left]] == 0):
                    contains.pop(s[left])

                
                left += 1

        return nice
