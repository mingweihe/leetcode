class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        dic = dict()
        self.res = 0

        def dfs(idx):
            if idx in dic: return dic[idx]
            ans = 1
            left, right = max(0, idx - d), min(len(arr) - 1, idx + d)
            j = idx
            while j > left and arr[idx] > arr[j - 1]:
                j -= 1
                ans = max(ans, dfs(j) + 1)
            j = idx
            while j < right and arr[idx] > arr[j + 1]:
                j += 1
                ans = max(ans, dfs(j) + 1)
            dic[idx] = ans
            self.res = max(self.res, ans)
            return ans

        for i in xrange(len(arr)):
            dfs(i)
        return self.res
