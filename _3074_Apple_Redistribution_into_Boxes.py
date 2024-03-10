class Solution(object):
    def minimumBoxes(self, a, c):
        """
        :type apple: List[int]
        :type capacity: List[int]
        :rtype: int
        """
        t = sum(a)
        res = 0
        c.sort()
        for x in c[::-1]:
            if t <= 0: break
            res += 1
            t -= x
        return res
