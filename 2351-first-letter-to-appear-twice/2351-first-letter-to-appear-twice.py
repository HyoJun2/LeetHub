class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
            if d[c] > 1:  # 두 번째로 등장하는 문자를 찾는 것이므로 '>'를 사용합니다.
                return c  # 반복된 문자를 반환합니다
