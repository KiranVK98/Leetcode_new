import random
class RandomizedSet:

    def __init__(self):
        self.contains = set()

    def insert(self, val: int) -> bool:
        if val not in self.contains:
            self.contains.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.contains:
            self.contains.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        ls = list(self.contains)
        return random.choice(ls)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()