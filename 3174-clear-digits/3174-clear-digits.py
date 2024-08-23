class Solution:
    def clearDigits(self, s: str) -> str:
        # while, 숫자를 지울 수 있는 조건 잘 살펴보기
        while s: # 문자열이 비어있지 않는 한 계속하겠다
            exist_number = False
            # 첫번째 숫자 찾아서 제거
            # 숫자 제거, 문자열 slicing 활용
            # 3번째 위치한 문자를 제거
            # s = s[:3] + s[4:]
            for i, c in enumerate(s):
                if c.isnumeric():
                    exist_number = True
                    if i == 0:
                        s = s[1:]
                    else:
                        s = s[:i-1] + s[i+1:]
                    break
            if not exist_number:
                break
        return s
