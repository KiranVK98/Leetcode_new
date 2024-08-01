class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        check_s = dict()

        for val in s:
            if val not in check_s:
                check_s[val] = 1
            else:
                check_s[val] += 1

        check_t = dict()

        for val in t:
            if val not in check_t:
                check_t[val] = 1
            else:
                check_t[val] += 1


        for key,value in check_t.items():
            if key not in check_s:
                return key

            else:
                if(value > check_s[key]):
                    return key