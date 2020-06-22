from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r = len(dungeon)
        c = len(dungeon[0])
        sol =[[0]*c for i in range(r)]
        sol[r-1][c-1] = 1 if dungeon[r-1][c-1] > 0 else (1 - dungeon[r-1][c-1])
        for i in range(r-2,-1,-1):
            sol[i][c-1] = max(sol[i+1][c-1] - dungeon[i][c-1],1)

        for j in range(c-2,-1,-1):
            sol[r-1][j] = max(sol[r-1][j+1] - dungeon[r-1][j],1)
            print(sol[r-1][j+1] - dungeon[r-1][j])      
        
        for i in range(r-2,-1,-1):
            for j in range(c-2,-1,-1):
                sol[i][j] = max(min(sol[i+1][j],sol[i][j+1]) - dungeon[i][j],1)
        print(sol)
        
        return sol[0][0]


points = [[-2, -3, 3], 
          [-5, -10, 1], 
          [10, 30, -5]]
result = Solution()
print(result.calculateMinimumHP(points))