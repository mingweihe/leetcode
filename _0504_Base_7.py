class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Approach 2
        if num < 0: return '-'+self.convertToBase7(-num)
        if num < 7: return str(num)
        return self.convertToBase7(num//7)+str(num%7)

        # Approach 1
        # if num == 0: return '0'
        # t = abs(num)
        # res = ''
        # while t:
        #     res = str(t % 7) + res
        #     t //= 7
        # return res if num > 0 else '-' + res
