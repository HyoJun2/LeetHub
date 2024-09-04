class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        nums = int(n/2)
        if n % 2 != 0:
            answer.append(0)
        for i in range(1, nums + 1):
            answer.append(i)
            answer.append(-i)
        return answer