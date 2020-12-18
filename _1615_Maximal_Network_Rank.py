class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        res = 0
        db = dict()
        for a, b in roads:
            db[a] = db.get(a, set())
            db[a].add(b)
            db[b] = db.get(b, set())
            db[b].add(a)
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                cur = len(db.get(i, [])) + len(db.get(j, [])) - (i in db.get(j, []) or j in db.get(i, []))
                res = max(cur, res)
        return res
