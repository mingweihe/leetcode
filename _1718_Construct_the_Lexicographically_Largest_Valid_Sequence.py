class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * ((n-1) * 2 + 1)
        used = [False] * (n + 1)
        L = len(ans)
        def dfs(idx):
            if idx == L: return True
            if ans[idx]: return dfs(idx + 1)
            for x in xrange(n, 0, -1):
                if used[x]: continue
                if x != 1 and (idx + x >= L or ans[idx + x]): continue
                ans[idx] = x
                if x != 1: ans[idx + x] = x
                used[x] = True
                if dfs(idx + 1): return True
                ans[idx] = 0
                if x != 1: ans[idx + x] = 0
                used[x] = False
            return False
        dfs(0)
        return ans
