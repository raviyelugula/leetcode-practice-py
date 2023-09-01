from typing import List 

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            bitstring = bin(i)
            count_ones = bitstring.count('1')
            result.append(count_ones)
        return result 
    
if __name__ == '__main__':
    print(Solution().countBits(5))