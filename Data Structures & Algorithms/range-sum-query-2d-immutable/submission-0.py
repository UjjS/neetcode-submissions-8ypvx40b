class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLUMN = len(matrix), len(matrix[0])
        self.Matsum= [[0]*(COLUMN+1) for i in range(0,ROWS +1)]

        for r in range(ROWS):
            prefix=0
            for c in range(COLUMN):
              prefix+= matrix[r][c]
              above = self.Matsum[r][c+1]
              self.Matsum[r+1][c+1] = prefix + above

                

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        r1 , c1 , r2 , c2 = r1+1 , c1+1, r2+1,c2+1
        bottomright = self.Matsum[r2][c2]
        above = self.Matsum[r1-1][c2]
        left = self.Matsum[r2][c1-1]
        topLeft= self.Matsum[r1-1][c1-1]

        return bottomright - above - left + topLeft



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)