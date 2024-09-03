class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # zip
        str_1 = str(num1).zfill(4)
        str_2 = str(num2).zfill(4)
        str_3 = str(num3).zfill(4)
        
        answer = []
        for i in range(4):
            answer.append(min(str_1[i], str_2[i], str_3[i]))
        return int("".join(answer))