class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Approach 2
        temp = []
        if len(a) < len(b):
            a = ('%0' + str(len(b)) + 'd') % int(a)
        else:
            b = ('%0' + str(len(a)) + 'd') % int(b)
        carry = 0
        for i in range(len(a) - 1, -1, -1):
            accum = carry + int(a[i]) + int(b[i])
            if accum > 1:
                carry = 1
                temp.insert(0, accum % 2)
            else:
                carry = 0
                temp.insert(0, accum % 2)
        if carry:
            return '1' + ''.join(map(str, temp))
        else:
            return ''.join(map(str, temp))

        # Approach 1
        # return bin(int(a, 2) + int(b, 2))[2:]
