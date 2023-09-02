from typing import List 

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, dictionary_set = len(s), set(dictionary)
        def dp(start):
            if start == n:
                return 0
            # To count this character as a left over character 
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
            return ans
            
        return dp(0)
    
if __name__ == "__main__":
     #s = "voctvochpgutoywpnafylzelqsnzsbandjcqdciyoefi"
     #dictionary = ["tf","v","wadrya","a","cqdci","uqfg","voc","zelqsn","band","b","yoefi","utoywp","herqqn","umra","frfuyj","vczatj","sdww"]
     #print(f'expected 11 - {Solution().minExtraChar(s, dictionary )}')
     s = "metzeaencgpgvsckjrqafkxgyzbe"
     dictionary = ["zdzz","lgrhy","r","ohk","zkowk","g","zqpn","anoni","ka","qafkx","t","jr","xdye","mppc","bqqb","encgp","yf","vl","ctsxk","gn","cujh","ce","rwrpq","tze","zxhg","yzbe","c","o","hnk","gv","uzbc","xn","kk","ujjd","vv","mxhmv","ugn","at","kumr","ensv","x","uy","gb","ae","jljuo","xqkgj"]
     print(f'expected 5 - {Solution().minExtraChar(s, dictionary )}')
     #s = "dwmodizxvvbosxxw"
     #dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
     #print(Solution().minExtraChar(s, dictionary ))
     

