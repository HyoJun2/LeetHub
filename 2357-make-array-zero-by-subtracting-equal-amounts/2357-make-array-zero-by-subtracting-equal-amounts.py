class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # 규칙 찾기
        # 0이 아닌 유니크한 숫자 개수
        answer = 0
        nums = set(nums)
        for i in nums:
            if 0 in nums:
                answer = 1
        return (len(nums) - answer)