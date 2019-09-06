import math


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # Approach 2
        return int(math.ceil(math.log(buckets)/math.log(minutesToTest/minutesToDie+1)))

        # Approach 1
        # res, a = 0, minutesToTest // minutesToDie + 1
        # while a ** res < buckets: res += 1
        # return res
