class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # Approach 1
        l, r = 1, num
        while l < r:
            mid = l+(r-l)//2
            if mid**2>num: r = mid - 1
            elif mid**2<num: l = mid + 1
            else: return True
        return l**2 == num
        # Approach 1
        # i = 1
        # while i ** 2 < num: i += 1
        # if i ** 2 == num: return True
        # return False
