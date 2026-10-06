class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i < j:
            mid = (i + j) // 2
            if (nums[mid] >= nums[i] and nums[mid] >= target and target >= nums[i]) \
                or (nums[mid] < nums[i] and (target >= nums[i] or target <= nums[mid])):
                j = mid
            else:
                i = mid + 1
        if nums[i] == target:
            return i
        else:
            return -1
