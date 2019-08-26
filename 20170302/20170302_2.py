class Solution:
    def updateBoard(self, board, click):
        by, bx = click[0], click[1]
        y = len(board)
        x = len(board[0])
        mines = 0;
        if board[by][bx] == 'E':
            if bx >= 0 and bx < x-1 and board[by][bx+1] == 'M':
                mines += 1
            if bx > 0 and bx <= x-1 and board[by][bx-1] == 'M':
                mines += 1
            if by >= 0 and by < y-1 and board[by+1][bx] == 'M':
                mines += 1
            if by > 0 and by <= y-1 and board[by-1][bx] == 'M':
                mines += 1
            if bx>=0 and by>=0 and bx<x-1 and by<y-1 and board[by+1][bx+1] == 'M':
                mines += 1
            if bx>0 and by>=0 and bx<=x-1 and by<y-1 and board[by+1][bx-1] == 'M':
                mines += 1
            if bx>=0 and by>0 and bx<x-1 and by<=y-1 and board[by-1][bx+1] == 'M':
                mines += 1
            if bx>0 and by>0 and bx<=x-1 and by<=y-1 and board[by-1][bx-1] == 'M':
                mines += 1
            board[by][bx] = str(mines)
            if board[by][bx] == '0':
                board[by][bx] = 'B'
            if mines == 0:
                if bx >= 0 and bx < x-1:
                    self.updateBoard(board, [by,bx+1])
                if bx > 0 and bx <= x-1:
                    self.updateBoard(board, [by,bx-1])
                if by >= 0 and by < y-1:
                    self.updateBoard(board, [by+1, bx])
                if by > 0 and by <= y-1:
                    self.updateBoard(board, [by-1, bx])
                if bx>=0 and by>=0 and bx<x-1 and by<y-1:
                    self.updateBoard(board, [by+1, bx+1])
                if bx>0 and by>=0 and bx<=x-1 and by<y-1:
                    self.updateBoard(board, [by+1, bx-1])
                if bx>=0 and by>0 and bx<x-1 and by<=y-1:
                    self.updateBoard(board, [by-1, bx+1])
                if bx>0 and by>0 and bx<=x-1 and by<=y-1:
                    self.updateBoard(board, [by-1, bx-1])
        elif board[by][bx] == 'M':
            board[by][bx] = 'X'
        return board
            
import unittest
class test_solution(unittest.TestCase):
    def test_all(self):
        s = Solution()
        i = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
        o = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]
        self.assertEqual(s.updateBoard(i, [3,0]), o)
        i = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'M', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']]
        o = [['B', '1', 'E', '1', 'B'],
             ['B', '1', 'X', '1', 'B'],
             ['B', '1', '1', '1', 'B'],
             ['B', 'B', 'B', 'B', 'B']] 
        self.assertEqual(s.updateBoard(i, [1,2]), o)

if __name__ == "__main__":
    unittest.main()
