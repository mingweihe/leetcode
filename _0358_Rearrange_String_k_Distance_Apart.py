from collections import Counter
from heapq import heapify, heappop, heappush
from collections import deque


class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 0: return s
        hq = [(-v, c) for c, v in Counter(s).items()]
        heapify(hq)
        res = ''
        qu = deque()
        while hq:
            cnt, c = heappop(hq)
            if cnt < 0:
                res += c
                cnt += 1
                qu.append((cnt, c))
            if len(qu) == k:
                release = qu.popleft()
                if release[0] < 0:
                    heappush(hq, release)
        return res if len(res) == len(s) else ''
