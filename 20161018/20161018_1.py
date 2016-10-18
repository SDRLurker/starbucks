class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        c = 0
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 'X':
                    adjent_cnt = 0
                    if y > 0 and board[y-1][x] == 'X':
                        adjent_cnt += 1
                    if x > 0 and board[y][x-1] == 'X':
                        adjent_cnt += 1
                    if adjent_cnt == 2:
                        return -1
                    elif adjent_cnt == 0:
                        c += 1
        return c

def solve_string(s, board, expected):
	return "%40s %10d %10d" % (board, expected, s.countBattleships(board))

s = Solution()
print("%40s %10s %10s" % ("board", "Expected", "Result"))
print(solve_string(s, ["X..X","...X","...X"], 2))
