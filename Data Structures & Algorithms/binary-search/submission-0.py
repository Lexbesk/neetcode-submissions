class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)

        while i + 1 < j:
            mid = (i + j) // 2
            if nums[mid] <= target:
                i = mid
            else:
                j = mid
        if nums[i] == target:
            return i
        return -1