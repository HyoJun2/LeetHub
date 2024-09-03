class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # 한변의 길이가 홀수일 때는 겹치는 중간값 한번 빼주기
        # 2중 for문
        n = len(mat)
        result = 0
        for i in range(n):
            result += mat[i][i] + mat[i][n - i - 1]
        if n % 2 == 1:
            result -= mat[n // 2][n // 2]
        return result