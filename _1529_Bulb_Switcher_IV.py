class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        cnt = 0
        target += '0'
        for i in xrange(1, len(target)):
            if target[i] == '0' and target[i-1] == '1':
                cnt += 1
        if cnt == 0: return 0
        if target[-2] == '0': return 2 * cnt
        return cnt * 2 - 1
