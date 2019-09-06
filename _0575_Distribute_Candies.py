class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # Approach 2
        return min(len(set(candies)), len(candies) / 2)

        # Approach 1
        # len_kinds = len(set(candies))
        # len_half = len(candies)/2
        # return len_kinds if len_kinds < len_half else len_half
