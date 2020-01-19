class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Approach 2
        return int(str(num).replace('6', '9', 1))

        # Approach 1
        # res = ''
        # num = str(num)
        # for i, c in enumerate(num):
        #     if c == '6':
        #         return int(res + '9' + num[i+1:])
        #     res += c
        # return int(res)
