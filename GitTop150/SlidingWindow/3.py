class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest = 0
        check = set()
        while(end < len(s)):
            if s[end] not in check:
                check.add(s[end])

            else:
                longest = max(longest, end-start)
                while(s[end] in check):
                    check.remove(s[start])
                    start += 1

                check.add(s[end])

            end+=1

        longest = max(longest, end-start)
        return longest
