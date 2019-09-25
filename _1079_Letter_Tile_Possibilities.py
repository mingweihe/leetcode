class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        res = set()

        def helper(cur, pool):
            if cur: res.add(cur)
            for i in xrange(len(pool)):
                helper(cur + pool[i], pool[:i] + pool[i+1:])
        helper('', tiles)
        return len(res)
