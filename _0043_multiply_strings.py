class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        digits = [0]*(m+n)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                product = int(num1[i])*int(num2[j])
                p1, p2 = i+j, i+j+1
                sums = digits[p2] + product
                digits[p1], digits[p2] = digits[p1]+sums/10, sums%10
        res = ''
        for i in digits:
            if not (res=='' and i==0): res += str(i)
        return res if res != '' else '0'
