class Solution:
    def minimumChairs(self, s: str) -> int:
        max_chairs = 0
        current_chairs = 0

        for i in s:
            if i == "E":
                current_chairs += 1
                max_chairs = max(max_chairs, current_chairs)
            else:
                current_chairs -= 1
        return max_chairs