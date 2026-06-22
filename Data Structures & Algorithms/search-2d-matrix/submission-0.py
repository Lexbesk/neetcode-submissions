class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_i = 0
        row_j = len(matrix)

        while row_i + 1 < row_j:
            mid = (row_i + row_j) // 2
            if matrix[mid][0] <= target:
                row_i = mid
            else:
                row_j = mid

        i = 0
        j = len(matrix[0])

        while i + 1 < j:
            mid = (i + j) // 2
            if matrix[row_i][mid] <= target:
                i = mid
            else:
                j = mid
        if matrix[row_i][i] == target:
            return True
        return False