class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = int(s[i - 2:i])
                i -= 3
            else:
                num = int(s[i])
                i -= 1
            res += chr(96 + num)
        return ''.join(reversed(res))
