class Solution:
    def addDigits(self, num: int) -> int:
        # while , 숫자 - 문자열 - 숫자
        # n = list(map(int, str(num)))
        while num > 9:
            num = num % 10 + num // 10
        return num