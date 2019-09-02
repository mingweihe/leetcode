class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or s == '':
            return 0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s) - 1):
            if dic[s[i + 1]] > dic[s[i]]:
                res -= dic[s[i]]
            else:
                res += dic[s[i]]
        res += dic[s[-1]]
        return res
