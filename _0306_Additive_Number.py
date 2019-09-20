class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        L = len(num)
        for i in xrange(1, L / 2 + 1):
            if num[0] == '0' and i > 1: return False
            num1 = num[:i]
            for j in xrange(i + 1, L):
                if num[i] == '0' and j > i + 1: break
                num2 = num[i:j]
                if self.is_valid(num1, num2, j, num):
                    return True
        return False

    def is_valid(self, n1, n2, start, num):
        if start == len(num): return True
        num1, num2 = int(n1), int(n2)
        n1, n2 = `num2`, `num1 + num2`
        return num.startswith(n2, start) and self.is_valid(n1, n2, start + len(n2), num)
