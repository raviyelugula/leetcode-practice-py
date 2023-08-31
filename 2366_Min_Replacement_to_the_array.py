from typing import List 
import math

class Solution:
    def minimumReplacement(self, nums):
        n, replacements, max = len(nums), 0, nums[-1]

        for i in range(n-2,-1,-1):
            req_splits = math.ceil(nums[i]/max)
            replacements += req_splits-1
            max = nums[i]//req_splits

        return replacements
    
if __name__ == "__main__":
    s = Solution()
    print(s.minimumReplacement([12,9,7,6,17,19,21]))
