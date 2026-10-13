class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fractorial(x: int):
            if x == 0 or x == 1:
                return 1
            else:
                res = 1
                for i in range(1, x+1):
                    res *= i
                return res
        return int(fractorial(m + n - 2) / (fractorial(n-1) * fractorial(m-1)))