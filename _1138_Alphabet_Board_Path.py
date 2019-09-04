import string


class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        res = ''
        m = {x:[i%5, i//5] for i,x in enumerate(string.ascii_lowercase)}
        x0, y0 = 0, 0
        for c in target:
            x, y = m[c]
            if y < y0: res += 'U'*(y0-y)
            if x < x0: res += 'L'*(x0-x)
            if y > y0: res += 'D'*(y-y0)
            if x > x0: res += 'R'*(x-x0)
            res += '!'
            x0, y0 = x, y
        return res
