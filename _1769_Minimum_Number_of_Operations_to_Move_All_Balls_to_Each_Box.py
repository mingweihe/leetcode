class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        n = len(boxes)
        res = [0] * n
        cur = total = 0
        for i, x in enumerate(boxes):
            cur += total
            res[i] = cur
            total += int(x)
        cur = total = 0
        for i in xrange(n-1, -1, -1):
            cur += total
            res[i] += cur
            total += int(boxes[i])
        return res
