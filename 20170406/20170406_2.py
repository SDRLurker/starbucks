class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ds = ((1,0), (0,1), (0,-1), (-1,0))
        for y in range(len(matrix)):
            for x in range(len(matrix[y])-1, -1, -1):
                if matrix[y][x] == 1:
                    d4 = []
                    for d in ds:
                        xx = x+d[0]
                        yy = y+d[1]
                        if 0 <= xx < len(matrix[y]) and 0 <= yy < len(matrix):
                            d4.append(matrix[yy][xx])
                        if len(d4) > 0:
                            matrix[y][x] = min(d4) + 1
        return matrix
        
