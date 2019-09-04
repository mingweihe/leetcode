class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2): num1, num2 = num2, num1
        l1, l2 = len(num1), len(num2)
        res, carry = '', 0
        for i in range(l1-1, -1, -1):
            s = int(num1[i]) + int(num2[l2-l1+i]) + carry
            res = str(s%10) + res
            carry = s//10
        for i in range(l2-l1-1, -1, -1):
            s = int(num2[i]) + carry
            res = str(s%10) + res
            carry = s//10
        if carry: res = '1' + res
        return res
