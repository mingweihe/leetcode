from collections import deque


class Solution(object):
    def findLexSmallestString(self, s, a, b):
        """
        :type s: str
        :type a: int
        :type b: int
        :rtype: str
        """
        def add(s):
            res = []
            for i, c in enumerate(s):
                int_c = int(c)
                if i % 2: res.append(str((int_c+a)%10))
                else: res.append(c)
            return ''.join(res)
        
        def rotate(s):
            return s[len(s) - b:] + s[:len(s) - b]
        
        qu = deque()
        qu.append(s)
        vis = set()
        vis.add(s)
        while(qu):
            cs = qu.popleft()
            ns = add(cs)
            if ns not in vis:
                vis.add(ns)
                qu.append(ns)
            ns = rotate(cs)
            if ns not in vis:
                vis.add(ns)
                qu.append(ns)
        return min(vis)
