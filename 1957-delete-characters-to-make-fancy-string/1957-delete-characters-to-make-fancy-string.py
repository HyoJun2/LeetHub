class Solution:
    def makeFancyString(self, s: str) -> str:
        answer = []
        for i in s:
            if len(answer) > 1 and i == answer[-1] == answer[-2]:
                answer.pop()
            answer.append(i)
        return ''.join(answer)