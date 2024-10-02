class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1억개의 숫자가 정렬되어 있는 nums
        # target: 1900
        # 알고리즘
        # 1. 중간에 위치한 숫자를 찾는다.
        # 2. target과 같다면 해당 위치가 정답
        # 3-1. 만약 target이 현재 위치의 숫자보다 크다면, 중간과 맨끝 사이에 target이 존재할 것
        # 3-2. 만약 target이 현재 위치의 숫자보다 작다면, 처음과 중간 사이에 target이 존재할 것
        # 4. 후보군을 좁혀서 다시 1부터 시작
        # l = 0
        # r = len(nums) - 1
        # answer = -1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     else:
        #         right = mid - 1
        #         break
        # return answer

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1