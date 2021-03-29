from collections import deque, defaultdict


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        st = set(org)
        ss = set()
        dq = deque()
        graph = defaultdict(set)
        degree = [0] * (len(org) + 1)
        for sq in seqs:
            for i, x in enumerate(sq):
                if x not in st: return False
                ss.add(x)
                if i == 0: continue
                if x not in graph[sq[i-1]]:
                    degree[x] += 1
                    graph[sq[i-1]].add(x)
        if st != ss: return False
        for i in xrange(1, len(org)+1):
            if degree[i] == 0:
                dq.append(i)
        idx = 0
        while dq:
            if len(dq) > 1: return False
            val = dq.popleft()
            if val != org[idx]: return False
            for nx in graph[val]:
                degree[nx] -= 1
                if degree[nx] == 0:
                    dq.append(nx)
            idx += 1
        return idx == len(org)
