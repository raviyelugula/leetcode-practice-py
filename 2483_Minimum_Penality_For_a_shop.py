class Solution:
    def bestClosingTime(self, customers: str) -> int:
        solp = customers.count('Y')
        print(f'initial solution is {solp}')
        index = 0
        for i in range(len(customers)+1): 
            p = 0 
            j = 0
            while j < len(customers):
                # open 
                if j < i and customers[j] == 'N':
                    p = p + 1
                elif j >= i and customers[j] == 'Y':
                    p = p + 1 
                j = j + 1
            if p < solp :
                print(f'p is {p} and solp is {solp} and index is {i} - altered ') 
                solp = p 
                index = i 
            else : 
                print(f'p is {p}  solp is {solp} and index is {i} -  ') 

        return index 

if __name__ == "__main__":
    s = Solution()
    print(s.bestClosingTime("YYNY"))
