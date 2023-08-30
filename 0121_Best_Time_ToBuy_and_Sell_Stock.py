from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = len(prices)
        sell = buy = prices[0]
        max_profit = 0 
        for i in range(1,L):
            if prices[i] < buy: 
                buy = prices[i]
            else:
                sell = prices[i]
                profit = sell - buy 
                if max_profit < profit: 
                    max_profit = profit 
        return max_profit 
    
if __name__ == '__main__':
        s = Solution()
        print(f'{s.maxProfit([7,1,5,3,6,4])} - expected 5')
        print(f'{s.maxProfit([7,6,4,3,1])}- expected 0')