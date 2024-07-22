class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        op = 0
        for i in range(len(students)):
            op += abs(students[i] - seats[i])


        return op
        