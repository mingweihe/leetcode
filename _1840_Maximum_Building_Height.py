class Solution(object):
    def maxBuilding(self, n, res):
        """
        :type n: int
        :type res: List[List[int]]
        :rtype: int
        """
        ans = 0
        res += [[1, 0], [n, n-1]]
        res.sort()
        m = len(res)
        for i in xrange(1, m):
            res[i][1] = min(res[i][1], res[i-1][1] + res[i][0] - res[i-1][0])
        for i in xrange(m-2, -1, -1):
            res[i][1] = min(res[i][1], res[i+1][1] + res[i+1][0] - res[i][0])
        for i in xrange(1, m):
            height_diff = abs(res[i][1] - res[i-1][1])
            dis = res[i][0] - res[i-1][0]
            height_extra = (dis - height_diff) / 2
            ans = max(ans, max(res[i][1], res[i-1][1]) + height_extra)
        return ans
