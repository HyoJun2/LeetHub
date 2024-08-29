class Solution:
    def reformatNumber(self, number: str) -> str:
        # replace, slice
        answer = []
        number = number.replace("-", "").replace(" ", "")
        for i in range(0, len(number), 3):
            if len(number) - i != 4:
                answer.append(number[i:i+3])
            else:
                answer.extend([number[i:i+2], number[i+2:]])
                break
        return '-'.join(answer)