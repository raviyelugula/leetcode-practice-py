"""
This question is about implementing a basic elimination algorithm for Candy Crush.
Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:
If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.

Example:
Input:
board = 
[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
Output:
[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
Explanation:
"""

from typing import List 


class Solution: 
    def candy_crush(self, board: List[List[int]]) -> List[List[int]]:
        
        need_crush = False 
        rows = len(board)
        columns = len(board[0])

        # scan horizonatally and indetify 3/more adjustcent cells  with the same value.
        for r in range(rows):
            for c in range(columns -2 ): 
                if abs(board[r][c]) == abs(board[r][c+1]) and abs(board[r][c+1]) == abs(board[r][c+2]) and board[r][c] != 0 :
                    board[r][c] = board[r][c+1] = board[r][c+2] = - abs(board[r][c])
                    need_crush = True 

        # scan vertically and indentify 3/more adjustcent cells with the same value.
        for c in range(columns): 
            for r in range(rows - 2):
                if abs(board[r][c]) == abs(board[r+1][c]) and abs(board[r+1][c]) == abs(board[r+2][c]) and board[r][c] != 0:
                    board[r][c] = board[r+1][c] = board[r+2][c] = - abs(board[r][c])
                    need_crush= True 

        # crush - this is column wise operation - find the first non negative value from the botton and drop it down - the left out top cells can be replaced with zeros
        if need_crush:
            for c in range(columns):
                anchor_row = rows -1 
                for r in range ( rows-1, -1, -1): # botton to the top ( oth element ) in desc.
                    if board[r][c] > 0 : 
                        board[anchor_row][c] = board[r][c]
                        anchor_row -=1 

                for r in range(anchor_row + 1):
                    board[r][c] = 0 
            
            return self.candy_crush(board)
        else: 
            return board


if __name__ == "__main__":
    s = Solution()
    print(s.candy_crush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))