import time

class Solution:
    def countPrimes(self, n: int) -> int:
        p = []
        for i in range(n):
            p.append(True)
        
        if n < 2: 
            return 0 
        else: 
            p[0]=p[1]= False 
            for i in range(2, n, 1):
                if p[i] == True: 
                    print(f' >> {i} checking')
                    for index in range(2*i, n, i):
                        p[index] = False 
            return sum(p)
        
if __name__ == "__main__":
    s = Solution()
    start_time = time.time()
    print(s.countPrimes(5000000))
    print(f'time taken {round(time.time() - start_time)} seconds')
        