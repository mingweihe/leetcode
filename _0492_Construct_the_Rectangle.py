class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # Approach 2
        W = int(area ** .5)
        for i in range(W, 0, -1):
            if area % i == 0: return [area / i, i]

        # Approach 1
        # W = int(area ** .5)
        # while area % W:
        #     W -= 1
        # return [area / W, W]
