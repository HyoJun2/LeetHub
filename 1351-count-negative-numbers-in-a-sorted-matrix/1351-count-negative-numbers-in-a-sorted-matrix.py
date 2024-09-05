class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    answer += 1
        return answer
