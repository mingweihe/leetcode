from itertools import izip_longest


class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Approach 2
        return [''.join(x).rstrip() for x in izip_longest(*s.split(), fillvalue=' ')]

        # Approach 1
        # arr = s.split()
        # L = max(map(len, arr))
        # res = []
        # for i in xrange(L):
        #     cur = ''
        #     for j in xrange(len(arr)):
        #         if i >= len(arr[j]): cur += ' '
        #         else: cur += arr[j][i]
        #     res += cur,
        # for i, s in enumerate(res):
        #     res[i] = res[i].rstrip()
        # return res
