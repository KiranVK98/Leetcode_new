class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0

        no_white = 0

        res = float('inf')
        for right in range(len(blocks)):
            if(blocks[right] == "W"):
                no_white += 1

            if(right - start + 1 == k):
                res = min(res, no_white)

                if(blocks[start] == "W"):
                    no_white -= 1

                start += 1


        return res