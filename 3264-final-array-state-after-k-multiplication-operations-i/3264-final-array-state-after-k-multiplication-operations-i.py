class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_value = min(nums)
            min_index = nums.index(min_value)
            # min_index 위치에 multiplier만큼 곱해주기
            nums[min_index] *= multiplier
        return nums