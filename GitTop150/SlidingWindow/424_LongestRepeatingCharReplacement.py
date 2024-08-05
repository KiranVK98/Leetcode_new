class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        left = 0

        max_length = 0


        for right in range(len(s)):
            if(s[right] not in count):
                count[s[right]] = 1

            else:
                count[s[right]] += 1

            max_count = 0
            for char, counts in count.items():
                max_count = max(max_count, counts)


            if((right -left + 1)  - max_count <= k):
                max_length = max(max_length, right - left + 1)

            else:
                count[s[left]] -= 1
                left += 1


        return max_length
