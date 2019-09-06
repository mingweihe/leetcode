class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # Approach 4
        return sum(map(J.count, S))

        # Approach 3
        # return sum([1 for c in S if c in J])

        # Approach 2
        # return sum([S.count(c) for c in J])

        # Approach 1
        # return len(re.sub('[^'+J+']', '', S))
