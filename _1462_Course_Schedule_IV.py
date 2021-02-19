from collections import defaultdict, deque


class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        preqs = {}
        parents = defaultdict(list)
        for a, b in prerequisites:
            parents[b] += a,
        for i in xrange(n):
            cur = set()
            qu = deque([i])
            while qu:
                node = qu.popleft()
                for nx in parents[node]:
                    if nx in cur: continue
                    cur.add(nx)
                    if nx in preqs:
                        cur |= preqs[nx]
                        continue
                    qu.append(nx)
            preqs[i] = cur
        return map(lambda x: x[0] in preqs[x[1]], queries)
