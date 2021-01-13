from collections import defaultdict


class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        roots = range(len(source))
        def find(x):
            if x != roots[x]:
                roots[x] = find(roots[x])
            return roots[x]
        
        for a, b in allowedSwaps:
            u = find(a)
            v = find(b)
            if u != v: roots[u] = v
        
        ## post processing way 1
        # res = 0
        # counter = defaultdict(Counter)
        # for i, (a, b) in enumerate(zip(source, target)):
        #     r = find(i)
        #     counter[r][a] += 1
        #     counter[r][b] -= 1
        # for k, v in counter.items():
        #     for diff in v.values():
        #         res += diff if diff > 0 else 0
        
        # post processing way 2
        res = len(source)
        indices = defaultdict(set)
        for i in xrange(len(roots)):
            indices[find(i)].add(i)
        for A in indices.values():
            cnt1, cnt2 = defaultdict(int), defaultdict(int)
            for idx in A:
                cnt1[source[idx]] += 1
                cnt2[target[idx]] += 1
            for k in cnt1.keys():
                res -= min(cnt1[k], cnt2[k])
        return res
