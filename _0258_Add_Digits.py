class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Approach 2
        return (num - 1) % 9 + 1 if num > 0 else 0

        # Approach 1
        # while num > 9: num = sum(map(int, list(str(num))))
        # return num
