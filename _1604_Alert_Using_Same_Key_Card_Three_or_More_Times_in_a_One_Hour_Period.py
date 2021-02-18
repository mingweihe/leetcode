class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        res = set()
        A = sorted(zip(keyName, keyTime))
        for i in xrange(2, len(A)):
            if A[i][0] != A[i-2][0]: continue
            a, b = A[i-2][1], A[i][1]
            diff_h = int(b[:2]) - int(a[:2])
            diff_m = int(b[3:]) - int(a[3:])
            diff = diff_h * 60 + diff_m
            if diff <= 60: res.add(A[i][0])
        return sorted(res)
