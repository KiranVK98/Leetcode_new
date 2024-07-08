class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        start=0
        end=len(s)-1
        s=s.lower()
        while(start < end):
            if(s[start] != s[end]):
                return False
            start+=1
            end-=1

        return True
    


test = Solution()
print(test.isPalindrome("A man, a plan, a canal: Panam"))

print(test)