class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # s1 = (ord(coordinate1[0]) - ord('a')) + int(coordinate1[1])
        # s2 = (ord(coordinate2[0]) - ord('a')) + int(coordinate2[1])
        # return s1 % 2 == s2 % 2

        x_1, y_1 = coordinate1
        x_2, y_2 = coordinate2

        # 알파벳을 숫자로 바꿔준 수와
        # 숫자를 더해준 값의 %2 값이 동일하면 같은 색!

        if (int(ord(x_1)) + int(y_1)) % 2 == (int(ord(x_2)) + int(y_2)) % 2:
            return True

        return False