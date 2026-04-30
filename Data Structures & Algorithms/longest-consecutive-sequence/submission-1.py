class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = 0
        for num in nums:
            if num - 1 in numbers:
                continue
            l = 1
            i = num + 1
            while i in numbers:
                l += 1
                i += 1
            res = max(l, res)
        return res
                
