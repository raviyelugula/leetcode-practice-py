from typing import List 
import math

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        open = min = max = 0 
        L = len(ranges)
        while max < n : 
            # By the end of for loop you need to get max moved else no possible tap to water uncovered garden
            for i in range(L): 
                if (i-ranges[i]) <= min and (i+ranges[i]) > max : 
                    max = i + ranges[i]
            if min == max : 
                return -1 # you are inside while i,e garden is not watered 
            else: 
                open +=1
                min = max 
        return open 
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.minTaps(5, [3,4,1,1,0,0]))
    print(s.minTaps(3, [0,0,0]))
