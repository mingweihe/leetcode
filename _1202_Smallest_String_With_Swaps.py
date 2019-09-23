import collections


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        if not pairs: return s
        res, roots = [], range(len(s))

        def find(ind):
            if roots[ind] != ind: roots[ind] = find(roots[ind])
            return roots[ind]

        for i, j in pairs:
            i, j = find(i), find(j)
            if i != j: roots[i] = j
        graphs = collections.defaultdict(list)
        for i in xrange(len(s)): graphs[find(i)].append(s[i])
        for v in graphs.values(): v.sort(reverse=True)
        for i in xrange(len(s)): res.append(graphs[find(i)].pop())
        return ''.join(res)
