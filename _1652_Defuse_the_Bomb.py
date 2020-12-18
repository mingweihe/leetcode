class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(code)
        res = [0] * n
        if k == 0: return res
        if k > 0:
            for i in xrange(n):
                j = (i + 1) % n
                cur = 0
                for p in xrange(k):
                    idx = (j + p) % n
                    cur += code[idx]
                res[i] = cur
        else:
            k = -k
            for i in xrange(n):
                j = i - 1
                cur = 0
                for p in xrange(k):
                    if j < 0: j = n-1
                    cur += code[j]
                    j -= 1
                    if j < 0: j = n-1
                res[i] = cur
        return res
