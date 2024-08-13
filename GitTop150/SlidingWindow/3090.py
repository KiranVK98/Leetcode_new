class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = collections.defaultdict(int)

        start = 0

        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1
            bad = False
            for char, counts in count.items():
                if(counts > 2):
                    bad = True


            if(bad):
                count[s[start]] -= 1 
                if(count[s[start]] == 0):
                    count.pop(s[start])
                start += 1

            else:
                # print(right,start)
                max_length = max(max_length, right-start+1)

        return max_length
