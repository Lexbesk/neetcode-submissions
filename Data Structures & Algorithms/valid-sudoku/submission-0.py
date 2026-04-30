class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check subboxes
        # print('checking')
        for b in range(9):
            seen = set()
            for i in range((b // 3) * 3, (b // 3 + 1) * 3):
                for j in range((b % 3) * 3, (b % 3 + 1) * 3):
                    if board[i][j] in seen:
                        return False
                    elif board[i][j] != '.':
                        seen.add(board[i][j])
        # print('checked boxed')
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen:
                    return False
                elif board[i][j] != '.':
                    seen.add(board[i][j])
        # print('checked rows')
        for j in range(9):
            seen = set()
            for i in range(9):
                if board[i][j] in seen:
                    return False
                elif board[i][j] != '.':
                    seen.add(board[i][j])
        return True