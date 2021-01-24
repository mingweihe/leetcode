from collections import Counter


class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        def helper():
            _a = 0
            _b = n
            res = float('inf')
            for i in xrange(25):
                divider = chr(97+i)
                _a += aa[divider]
                _b -= bb[divider]
                to_change_a = m - _a
                to_change_b = n - _b
                res = min(res, to_change_a + to_change_b)
            return res
            
        m, n = len(a), len(b)
        aa, bb = Counter(a), Counter(b)
        a_b = a + b
        ab = Counter(a_b)
        cost3 = len(a_b) - sorted(ab.values(), reverse=True)[0]
        
        cost1 = helper()
        
        m, n = len(b), len(a)
        aa, bb = Counter(b), Counter(a)
        
        cost2 = helper()
        return min(cost1, cost2, cost3)
