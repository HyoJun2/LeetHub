class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # sorting
        answer = 0
        seats = sorted(seats)
        students = sorted(students)
        
        for i in range(len(seats)):
            answer += abs(seats[i] - students[i])

        return answer             
        