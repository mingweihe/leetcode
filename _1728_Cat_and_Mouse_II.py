class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        @lru_cache(None)
        def dp(mouse, cat, moves):
            if cat == mouse: return False
            if cat == food: return False
            if moves == max_moves: return False
            if mouse == food: return True
            # mouse's turn
            if moves & 1 == 0:
                for k in range(4):
                    for jump in range(mouseJump+1):
                        ni = mouse[0] + dirs[k] * jump
                        nj = mouse[1] + dirs[k+1] * jump
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != '#':
                            if dp((ni, nj), cat, moves + 1): return True
                        else: break
                return False
            # cat's turn
            else:
                for k in range(4):
                    for jump in range(catJump+1):
                        ni = cat[0] + dirs[k] * jump
                        nj = cat[1] + dirs[k+1] * jump
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != '#':
                            if not dp(mouse, (ni, nj), moves + 1): return False
                        else: break
                return True
                
        m, n = len(grid), len(grid[0])
        cat = mouse = food = None
        max_moves = m * n * 2
        dirs = [-1, 0, 1, 0, -1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'C':
                    cat = (i, j)
                elif grid[i][j] == 'M':
                    mouse = (i, j)
                elif grid[i][j] == 'F':
                    food = (i, j)
        return dp(mouse, cat, 0)
