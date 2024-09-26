class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # 중복을 먼저 제거 hill, valley 카운팅
        hill_Valley = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                hill_Valley += 1
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                hill_Valley += 1
        return hill_Valley