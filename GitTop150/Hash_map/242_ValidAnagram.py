class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_array = [0] * 26
        if(len(s) != len(t)):
            return False

        for st in s:
            char_array[ord(st) - ord('a')] += 1

        
        for st in t:
            char_array[ord(st) - ord('a')] -= 1
        
        for count in char_array:
            if(count!=0):
                return False

        return True
