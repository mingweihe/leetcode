class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Approach 1
        return False if num < 6 else sum(i + num / i for i in range(2, int(num ** .5) + 1) if num % i == 0) + 1 == num
        # Approach 2
        # a=[ 6, 28, 496, 8128, 33550336]
        # if num in a: return True
        # else: return False

