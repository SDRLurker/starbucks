class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for y in range(9):
            num_set = set()
            for x in range(9):
                if board[y][x] != '.' and board[y][x] in num_set:
                    return False
                num_set.add(board[y][x])
        for x in range(9):
            num_set = set()
            for y in range(9):
                if board[y][x] != '.' and board[y][x] in num_set:
                    return False
                num_set.add(board[y][x])
        for yy in range(0, 9, 3):
            for xx in range(0, 9, 3):
                num_set = set()
                for y in range(3):
                    for x in range(3):
                        if board[yy+y][xx+x] != '.' and board[yy+y][xx+x] in num_set:
                            return False
                        num_set.add(board[yy+y][xx+x])
        return True

def solve_string(s, board, expected):
    board_str = ""
    for i, row in enumerate(board):
        if i < 8:
            board_str += row + "\n"
        else:
            board_str += row
    return "%10s %10s %10s" % (board_str, expected, s.isValidSudoku(board))

s = Solution()
print("%10s %10s %10s" % ("board", "Expected", "Result"))
print(solve_string(s, [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"], True))
