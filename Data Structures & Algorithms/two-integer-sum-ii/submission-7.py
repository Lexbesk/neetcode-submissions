class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i < len(numbers):
            residual = target - numbers[i]
            j = 0
            while j < len(numbers) and numbers[j] <= residual:
                if numbers[j] == residual and i != j:
                    return [i+1, j+1]
                j += 1
            i += 1
        return [-1, -1]