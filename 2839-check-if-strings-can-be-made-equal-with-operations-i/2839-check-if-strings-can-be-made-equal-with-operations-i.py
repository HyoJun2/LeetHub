class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # swap을 통해서 새롭게 만들 수 있는 경우의 수가 제한됨!
        # 0 <-> 2
        # 1 <-> 3
        # 둘다 선택
        # for i in range(2):
        #     if s1[i] == s2[i] or s1[i] == s2[i+2]:
        #         if s1[i] == s2[i]:
        #             continue
        #         else:
        #             s2_list = list(s2)
        #             s2_list[i], s2_list[i+2] = s2_list[i+2], s2_list[i]
        #             s2 = ''.join(s2_list)
        #     else:
        #         return False

        # if s1[3] == s2[3] and s1[2] == s2[2]:
        #     return True
        # return False

        new_str_1 = s1[2] + s1[1] + s1[0] + s1[3]
        new_str_2 = s1[0] + s1[3] + s1[2] + s1[1]
        new_str_3 = s1[2] + s1[3] + s1[0] + s1[1]

        # s2와 일치하는게 하나라도 있으면 True, 없으면 False

        if new_str_1 == s2 or new_str_2 == s2 or new_str_3 == s2:
            return True
        return False
