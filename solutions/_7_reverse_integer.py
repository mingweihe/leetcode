class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Method 1
        if x == 0: return 0
        res, sign = 0, int(abs(x)/x)
        x=abs(x)
        while x != 0:
            res = res*10 + x%10
            x = int(x/10)
        if res < -pow(2,31) or res >= pow(2, 31): return 0
        return res*sign

        # Method 2
        # s=str(x)
        # if s[0] == '-':
        #     s='-'+s[1:][::-1]
        # else:
        #     s=s[::-1]
        # res=int(s)
        # if res >= pow(2, 31) or res < -pow(2,31):
        #     return 0
        # return res
