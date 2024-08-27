class Solution:
    def makeFancyString(self, s: str) -> str:
        # answer = []
        # for i in s:
        #     if len(answer) > 1 and i == answer[-1] == answer[-2]:
        #         answer.pop()
        #     answer.append(i)
        # return ''.join(answer)

        # answer = ""
        # prev = ""
        # cnt = 0
        # for c in s:
        #     if c == prev:
        #         cnt += 1:
        #     else:
        #         cnt = 1:
        #     if cnt < 3:
        #         answer.append(c)
        #     return answer

        answer = []
        prev = ""
        cnt = 0
        for c in s:
            if c == prev:
                cnt += 1
            else:
                cnt = 1
            
            if cnt < 3:
                answer.append(c)
            
            prev = c
        
        return ''.join(answer)