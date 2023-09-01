from typing import List 
import collections


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

        ## create a dict with Lists 
        g = collections.defaultdict(list)
        for e1, e2 in adjacentPairs:
            g[e1].append(e2)
            g[e2].append(e1)
        
        ## find the starting/ending element i,e with len 1 
        for key, value in g.items():
            if len(value)==1: 
                start = key 
                break 
        
        visited = set()
        collection = []
        
        ## call dfs 
        def dfs(s):
            collection.append(s)
            visited.add(s)
            for value in g[s]:
                if value not in visited:
                    dfs(value)
        
        dfs(start)

        return collection 
    
if __name__ == "__main__":
    s = Solution()
    print(s.restoreArray([[4,-2],[1,4],[-3,1]]))