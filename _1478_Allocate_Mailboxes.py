class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:

        def get_medium(i, j):
            ans = None
            if j - i & 1:
                mid1 = (j + i) >> 1
                mid2 = mid1 + 1
                ans = (houses[mid1] + houses[mid2]) / 2
            else:
                ans = houses[(j+i) >> 1]
            return ans 
            
        @lru_cache(None)
        def dfs(i, j, k):
            if k == 0:
                if i <= j: return float('inf')
                else: return 0
            ans = float('inf')
            for end in range(i, j+1):
                medium = get_medium(i, end)
                cur = sum([abs(houses[idx]-medium) for idx in range(i, end+1)])
                ans = min(ans, cur + dfs(end+1, j, k-1))
            return ans
        houses.sort()
        return int(dfs(0, len(houses)-1, k))
