class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        i = 0
        for x in xrange(1, n+1):
            if x != target[i]:
                res += ['Push', 'Pop']
            else:
                res += 'Push',
                i += 1
            if i == len(target):
                break
        return res
