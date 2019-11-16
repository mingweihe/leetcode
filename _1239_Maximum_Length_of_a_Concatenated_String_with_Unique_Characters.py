class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        def dfs(cur, pos, cnt):
            if pos == len(arr):
                self.res = max(self.res, cnt)
                return
            new_set = cur | set(arr[pos])
            if len(new_set) == cnt + len(arr[pos]):
                dfs(new_set, pos+1, cnt + len(arr[pos]))
            dfs(cur, pos+1, cnt)
        self.res = 0
        dfs(set(), 0, 0)
        return self.res
