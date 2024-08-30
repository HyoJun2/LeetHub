class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        answer = 0
        for i in nums:
            if i < k:
                answer += 1
        return answer