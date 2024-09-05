class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for x in range(n)] for y in range(m)]

        for row, col in indices:
            for i in range(n):
                # 특정 row의 값을 1씩 증가시켜주기
                matrix[row][i] += 1
            for i in range(m):
                # 특정 column 값을 1씩 증가시켜주기
                matrix[i][col] += 1
        # 전체 matrix 순회하면서 홀수 개수 세어서 리턴
        answer = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 != 0:
                    answer += 1
        return answer