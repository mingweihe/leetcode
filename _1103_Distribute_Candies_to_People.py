class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0]*num_people
        i = 0
        while candies > 0:
            cur = i+1
            res[i%num_people] += cur
            candies -= cur
            i += 1
        res[(i-1)%num_people] += candies
        return res
