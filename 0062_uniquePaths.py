import time
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # last row where the each cell has a solution if moves right 
        row = [1] * n

        # calculate the other rows 
        for i in range(m-1):
            newRow = [1]*n 
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1]+row[j]
            row = newRow
        return row[0]