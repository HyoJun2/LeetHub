class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        #for, zip
        answer = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                answer += 1
        return answer