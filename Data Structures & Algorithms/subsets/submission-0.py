class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def _subsets(nums):
            if len(nums) == 0:
                return [[]]
            partial_subsets = _subsets(nums[1:])
            _output = []
            for subset in partial_subsets:
                _output.append(subset)
                new_subset = subset.copy()
                new_subset.append(nums[0])
                _output.append(new_subset)
            return _output
        
        return _subsets(nums)