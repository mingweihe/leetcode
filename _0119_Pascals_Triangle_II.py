class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            mid = (i + 2) >> 1
            t = 1
            for j in range(1, i):
                if j < mid:
                    res[j] = res[j] + t
                    t = res[j] - t
                else:
                    res[j] = res[i - j]
        return res
