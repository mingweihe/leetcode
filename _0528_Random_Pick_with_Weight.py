from random import randint
from bisect import bisect_left


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.pre = [0]
        for x in w:
            self.pre += x + self.pre[-1],
        
    def pickIndex(self):
        """
        :rtype: int
        """
        x = randint(1, self.pre[-1])
        return bisect_left(self.pre, x) - 1



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
