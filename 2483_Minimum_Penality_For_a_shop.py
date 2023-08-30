class Solution:
    def bestClosingTime(self, customers: str) -> int:
        toal_good_customers = customers.count('Y')
        best_i = 0 
        min_penality = toal_good_customers
        total_cust = len(customers)
        
        missed_good_customers = toal_good_customers
        found_bad_customer = 0 
        penality = 0 
        for i in range(0, total_cust+1): 
            if i < total_cust:
                if customers[i] == 'Y':
                    missed_good_customers = missed_good_customers - 1 
                else : 
                    found_bad_customer = found_bad_customer + 1 
                penality = missed_good_customers + found_bad_customer
                
            else : 
                penality = found_bad_customer
                
            if penality < min_penality: 
                min_penality = penality
                best_i = i +1
            
        return best_i
    
    def bestClosingTime_alternative(self, customers: str) -> int:
        # Instead of computing the minimum penalty, we can compute the max profit.
        ans = 0
        profit = 0
        maxProfit = 0
        for i, customer in enumerate(customers):
            profit += 1 if customer == 'Y' else -1
            if profit > maxProfit:
                maxProfit = profit
                ans = i + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(f'{s.bestClosingTime("YYNY")} - expected is 2')
    print(f'{s.bestClosingTime("NNNNN")} - expected is 0')
    print(f'{s.bestClosingTime("YYYY")} - expected is 4')
