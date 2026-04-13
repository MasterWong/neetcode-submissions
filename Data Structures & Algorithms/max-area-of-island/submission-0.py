class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        area = 0

        def dfs(a, b) -> int:
            if a < 0 or a >= len(grid):
                return 0
            if b < 0 or b >= len(grid[a]):
                return 0
            if (a, b) in visited:
                return 0
            visited.add((a,b))
            if grid[a][b] == 0:
                return 0
            
            count = 1
            count += dfs(a+1, b)
            count += dfs(a-1, b)
            count += dfs(a, b+1)
            count += dfs(a, b-1)
            return count

        
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr = dfs(i, j)
                    area = max(curr, area)

        return area
