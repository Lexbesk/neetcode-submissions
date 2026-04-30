class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [1 for i in range(l)]
        suffix = [1 for i in range(l)]
        for i in range(1, l):
            prefix[i] = prefix[i-1] * nums[i-1]
            suffix[l-i-1] = suffix[l-i] * nums[l-i]
        result = [prefix[i] * suffix[i] for i in range(l)]
        return result