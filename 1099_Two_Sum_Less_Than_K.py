"""
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""
from typing import List

class Solution:
    def twoSumLessThanK(self, A: List[int], k : int) -> int:
        L = len(A)
        max_s_lt_k = -1 
        for i, num in enumerate(A):
            j = i + 1 

            while j < L:     
                sum = num + A[j]
                if sum < k and sum > max_s_lt_k:
                    max_s_lt_k = sum 
                
                j = j + 1 
        return max_s_lt_k
    
if __name__ == '__main__':
    s = Solution()
    print(f'A = [10,20,30], K = 15, expected-ans -1,  {s.twoSumLessThanK([10,20,30], 15)}')
    print(f'A = [34,23,1,24,75,33,54,8], K = 60, expected-ans 58, {s.twoSumLessThanK([34,23,1,24,75,33,54,8], 60)}')
