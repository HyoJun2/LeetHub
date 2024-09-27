class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        answer = 0
        for i in range(0, len(colors)):
            for j in range(len(colors)-1, 0, -1):
                if colors[i] != colors[j] and j > i:
                    answer = max(answer, j-i)
        return answer        
