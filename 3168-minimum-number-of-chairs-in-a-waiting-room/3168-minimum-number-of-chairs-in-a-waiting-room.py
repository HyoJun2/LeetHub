class Solution:
    def minimumChairs(self, s: str) -> int:
        # max_chairs = 0
        # current_chairs = 0

        # for i in s:
        #     if i == "E":
        #         current_chairs += 1
        #         max_chairs = max(max_chairs, current_chairs)
        #     else:
        #         current_chairs -= 1
        # return max_chairs

        answer = 0
        cnt = 0
        for c in s:
            if c == "E":
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt -= 1
            # 방안에 머무는 사람의 최대 수를 answer로 지정
        return answer