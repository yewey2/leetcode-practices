from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        def helper(state, paths):
            # print(state, paths)
            # if not state or not all(state):
            x, y = len(state), len(state[0])
            if (x,y) in cache: 
                return cache[x,y]

            if state[0][0]==1:
                cache[x,y]=0
                return 0
            if len(state)==1 and len(state[0])==1:
                cache[x,y] = 1
                return 1

            if len(state) >= 2:
                a = helper(state[1:], paths) if state[1][0] == 0 else 0
                cache[x-1, y] = a
            else:
                a = 0
            if len(state[0])>=2:
                b = helper([i[1:] for i in state], paths) if state[0][1] == 0 else 0
                cache[x, y-1] = b
            else:
                b = 0
            # print(a+b)
            return a+b
        return helper(obstacleGrid, 1)

if __name__ == "__main__":
    s = Solution()
    tests = [
        ([[0,0,0],[0,1,0],[0,0,0]], 2),
        ([[0,1],[0,0]], 1),
        ([[0]], 1),
        ([[1]], 0),
        ([[0,0],[0,0]], 2),
    ]
    for grid, expected in tests:
        got = s.uniquePathsWithObstacles(grid)
        print(f"grid={grid} => {got} (expected {expected})")
