class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []

        for i in range(len(names)):
            res.append([heights[i],names[i]])

        res.sort(reverse=True)
        res_1 = []
        for i in res:
            res_1.append(i[1])

        return res_1


        