from typing import List
import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return 
        
        tkts_dict = collections.defaultdict(list)
        
        for src,dest in tickets:
            tkts_dict[src].append(dest)
            
        routes = ['JFK']
        
        def dfs(src):
            if len(routes) == len(tickets) + 1:
                return True
            destinations = sorted(tkts_dict[src])
            
            for destination in destinations:
                routes.append(destination)
                tkts_dict[src].remove(destination)
                if dfs(destination):
                    return True
                tkts_dict[src].append(destination)
                routes.pop()
                
        
        dfs('JFK')
        return routes

result = Solution()
print(result.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))