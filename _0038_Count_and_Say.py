class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n - 1):
            res = self.say(res)
        return res

    def say(self, seq):
        if len(seq) == 1:
            return '1' + seq
        cur = seq[0]
        res, num = '', 1
        for i in range(1, len(seq)):
            if seq[i] == cur:
                num += 1
            else:
                res += str(num) + cur
                cur, num = seq[i], 1
        res += str(num) + cur
        return res
