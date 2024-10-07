class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        answer = 0

        for i in range(len(s)):
            if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                answer -= d[s[i]]
            else:
                answer += d[s[i]]
        return answer