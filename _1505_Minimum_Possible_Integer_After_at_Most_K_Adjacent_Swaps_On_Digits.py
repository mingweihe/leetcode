import string
from collections import defaultdict, deque


class Solution(object):
    def minInteger(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        N = len(num)
        tree = [0] * (N * 2)
        def update(idx):
            idx += N
            tree[idx] += 1
            while idx > 1:
                tree[idx >> 1] = tree[idx] + tree[idx ^ 1]
                idx >>= 1
                
        def get_offset(j, i = 0):
            i, j = i + N, j + N
            ans = 0
            while i <= j:
                if i & 1:
                    ans += tree[i]
                    i += 1
                if j & 1 == 0:
                    ans += tree[j]
                    j -= 1
                i >>= 1
                j >>= 1  
            return ans

        res = []
        d = defaultdict(deque)
        for i, x in enumerate(num):
            d[x].append(i)
        while len(res) != N:
            for c in string.digits:
                if not d[c]: continue
                offset = get_offset(d[c][0])
                if k >= d[c][0] - offset:
                    idx = d[c].popleft()
                    k -= idx - offset
                    res += c,
                    update(idx)
                    break
        return ''.join(res)
