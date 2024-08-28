class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # 앞에 있는데 사고 싶은 티켓 수가 작은 경우
        # 앞에 있는데 사고 싶은 티켓이 많은 경우
        # 뒤에 있는데 사고 싶은 티켓이 많은 경우
        # 뒤에 있는데 사고 싶은 티켓이 작은 경우
        answer = 0
        for i in range(len(tickets)):
            if i <= k:
                if tickets[i] <= tickets[k]:
                    # 자기 사고 싶은 티켓 수만 사고 줄을 떠남
                    answer += tickets[i]
                else:
                    # 내가 사고 싶은 양을 살때까지 내 앞에 있음
                    answer += tickets[k]
            else:
                if tickets[i] < tickets[k]:
                    # 자기 사고 싶은 만큼만 사고 떠남
                    answer += tickets[i]
                else:
                    # 내가 사고 싶은 양 살때까지 줄에 머무는데, 나보다 뒤에 있어서
                    # 내가 다 사게 되는 시점에는 이 사람을 안기다려도 됨
                    answer += (tickets[k] - 1)
        return answer
