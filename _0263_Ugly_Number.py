class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while True:
            t = num
            if t % 5 == 0: t /= 5
            if t % 3 == 0: t /= 3
            if t % 2 == 0: t /= 2
            if t == 1: return True
            if t == num: return False
            num = t

