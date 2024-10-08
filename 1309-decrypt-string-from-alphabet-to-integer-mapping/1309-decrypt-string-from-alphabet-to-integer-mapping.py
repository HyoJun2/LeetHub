class Solution:
    def freqAlphabets(self, s: str) -> str:
        # answer = ""
        # i = len(s) - 1
        # while i >= 0:
        #     if s[i] == "#":
        #         answer = answer + chr(int(s[i-2:i]) + 96)
        #         i = i - 2
        #     else:
        #         answer = answer + chr(int(s[i]) + 96)
        #     i -= 1
        # return answer [::-1]

        # 각 알파벳과 숫자 표기를 매핑한 딕셔너리 만들기
        d = {}
        for i in range(26):
            alphabet = chr(i + 97)
            num = i + 1
            if num < 10:
                d[str(num)] = alphabet
            else:
                d[str(num) + "#"] = alphabet
        sorted_keys = sorted(d.keys(), reverse=True, key=lambda x: (len(x), x))
        # 반복문 사용해서 앞에서부터 문자열 매칭해서
        # 일치하는 숫자부터 문자열에서 제거하기
        answer = ""
        while s:
            for key in sorted_keys:
                if s.startswith(key):
                    answer += d[key]
                    s = s[len(key):]
                    break
        return answer
