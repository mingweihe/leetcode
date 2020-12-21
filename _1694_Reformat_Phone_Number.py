class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        res = []
        num = number.replace(' ', '').replace('-', '')
        for i in xrange(0, len(num), 3):
            res += num[i:i+3],
        if len(res) >= 2 and len(res[-1]) == 1:
            rest = res[-2] + res[-1]
            rest = [rest[:2], rest[2:]]
            res = res[:len(res)-2] + rest
        return '-'.join(res)
