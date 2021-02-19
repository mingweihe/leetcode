class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        ## Approach 2, conciser
        return sum(sorted(piles)[len(piles)/3::2])
        
        ## Approach 1
        # piles.sort()
        # res, each, n = 0, len(piles) / 3, len(piles)
        # for i in xrange(each, n, 2):
        #     res += piles[i]
        # return res
