import time
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        def findSolution(i,j):
            print(i,j)
            if i ==(m-1) and j == (n-1):
                return 1
            if i >=m or j >=n:
                return 0 
            return findSolution(i+1,j) + findSolution(i, j+1)
        """
        """
        def findSolution_dp(i,j):
            #print(i,j)
            if i ==(m-1) and j == (n-1):
                return 1
            if i >=m or j >=n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j] =  (findSolution_dp(i+1,j) + findSolution_dp(i, j+1))
            return dp[i][j]
        return findSolution_dp(0,0)
        
if __name__ == '__main__':
    s = time.time()
    m, n = 3, 7 
    dp = [[-1]*(n+1)]*(m+1)
    print(dp)
    print(Solution().uniquePaths(m,n))
    print(dp)
    print(f'{(time.time() - s)//60} seconds')