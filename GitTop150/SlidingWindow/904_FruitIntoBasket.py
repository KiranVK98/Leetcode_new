class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hash_map = {}

        #in a subarray there has to be at most two different fruits
        #we need maximum fruits that we an collect within this sub array

        left = 0


        max_fruits = 0

        for right in range(len(fruits)):
            if(len(hash_map) <= 2):
                if(fruits[right] not in hash_map):
                    hash_map[fruits[right]] = 1
                    # print(right)
                else:
                    hash_map[fruits[right]] += 1

                # print(left,right,hash_map,len(hash_map))
                if(len(hash_map) <= 2):
                    max_fruits = max(max_fruits, right - left+1)
                else:
                    max_fruits = max(max_fruits, right - left)




            else:
                if(fruits[right] not in hash_map):
                    hash_map[fruits[right]] = 1
                    # print(right)
                else:
                    hash_map[fruits[right]] += 1
                while(left < right and len(hash_map) > 2):
                    if(hash_map[fruits[left]] == 1):
                        del[hash_map[fruits[left]]]
                    else:
                        hash_map[fruits[left]] -= 1

                    # max_fruits = max(max_fruits, right - left)
                    left += 1
                    # print(hash_map)

                # print(left, right)
                max_fruits = max(max_fruits, right - left+1)
                




        return max_fruits

            