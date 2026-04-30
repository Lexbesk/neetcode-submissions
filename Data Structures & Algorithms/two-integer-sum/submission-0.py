class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        for i in range(len(nums)):
            if nums[i] in record:
                return [record[nums[i]], i]
            else:
                if target - nums[i] in record:
                    continue
                record[target - nums[i]] = i