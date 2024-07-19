class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_mag = dict()

        for i in magazine:
            hash_mag[i] = 1+ hash_mag.get(i,0)


        hash_ransom =dict()
        for i in ransomNote:
            hash_ransom[i] = 1+ hash_ransom.get(i,0)


        for key, value in hash_ransom.items():
            if(key in hash_mag):
                if(value > hash_mag[key]):
                    return False

            else:
                return False


        return True