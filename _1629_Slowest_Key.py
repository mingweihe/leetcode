from collections import defaultdict


class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        cnts = defaultdict(int)
        for i in xrange(len(releaseTimes)):
            if i == 0: cnts[keysPressed[i]] = releaseTimes[i]
            else: cnts[keysPressed[i]] = max(cnts[keysPressed[i]], releaseTimes[i] - releaseTimes[i-1])
        sorted_arr = sorted(cnts.items(), key=lambda x: (-x[1], -ord(x[0])))
        return sorted_arr[0][0]
