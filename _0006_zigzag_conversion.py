class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Approach 2
        if numRows <= 1: return s
        res = ['']*numRows
        index, step = 0, 1
        for i, x in enumerate(s):
            res[index] += x
            if index == 0: step = 1
            elif index == numRows-1: step = -1
            index += step
        return ''.join(res)
        # Approach 1
        # if numRows <= 1: return s
        # res = ['']*numRows
        # for i, x in enumerate(s):
        #     size = numRows*2-2
        #     index = i % size
        #     if index >= numRows:
        #         index = size - index
        #     res[index] += x
        # return ''.join(res)
