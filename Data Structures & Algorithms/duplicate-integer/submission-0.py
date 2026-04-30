class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appearance_num = {}
        for i in range(len(nums)):
            if nums[i] not in appearance_num:
                appearance_num[nums[i]] = 1
            else:
                return True
        return False