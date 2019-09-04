class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        cnt = 1
        res = [0, 0]
        line = 100
        ind = 0
        while ind < len(S):
            font_x = widths[ord(S[ind])-ord('a')]
            if line - font_x > -1:
                line -= font_x
                ind += 1
            else:
                line = 100
                cnt += 1
        res[0] = cnt
        res[1] = 0 if line == 0 else 100-line
        return res
