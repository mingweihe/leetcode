class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        accum_oxr = [0]
        for x in arr:
            accum_oxr += accum_oxr[-1] ^ x,
        res = []
        for l, r in queries:
            res += accum_oxr[l] ^ accum_oxr[r+1],
        return res
