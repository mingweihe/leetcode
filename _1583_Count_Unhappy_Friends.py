class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        rank = {}
        for i in xrange(n):
            for j, x in enumerate(preferences[i]):
                rank[i, x] = j
        paired = [0] * n
        for a, b in pairs:
            paired[a] = b
            paired[b] = a
        res = set()
        for x in xrange(n-1):
            for u in xrange(x+1, n):
                if paired[x] == u: continue
                y = paired[x]
                v = paired[u]
                if rank[x, u] < rank[x, y] and rank[u, x] < rank[u, v]:
                    res.add(x)
                    res.add(u)
        return len(res)
