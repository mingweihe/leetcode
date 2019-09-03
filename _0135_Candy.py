class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
            simple implementation problem, no trick
                loop from left to right
                loop from right to left
        """
        L = len(ratings)
        candies = [1] * L
        for i in xrange(1, L):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in xrange(L - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
