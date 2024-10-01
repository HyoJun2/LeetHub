class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        answer += 1
        return answer

        