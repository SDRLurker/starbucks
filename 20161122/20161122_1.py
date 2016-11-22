class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        p = 0
        adjent = ((-1,0), (0,1), (1,0), (0,-1))
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if grid[y][x] == 1:
                    cp = 0
                    for a in adjent:
                        if y+a[0] >= 0 and x+a[1] >= 0 and y+a[0] < len(grid) and x+a[1] < len(row) and grid[y+a[0]][x+a[1]] == 1:
                            cp += 1
                    p += (4-cp)
        return p

def solve_string(s, grid, expected):
    grid_str = ""
    for y, row in enumerate(grid):
        if y < len(grid) - 1:
            grid_str += str(row) + "\n"
        else:
            grid_str += str(row)
    return "%20s %10s %10d" % (grid_str, expected, s.islandPerimeter(grid))

s = Solution()
print("%12s %10s %10s" % ("grid", "Expected", "Result"))
print(solve_string(s, [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], 16))
