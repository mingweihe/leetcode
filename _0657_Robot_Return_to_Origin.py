class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # Approach 2
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

        # Approach 1
        # u,d,l,r = 0,0,0,0
        # for x in moves:
        #     if x == 'U': u += 1
        #     elif x == 'D': d += 1
        #     elif x == 'L': l += 1
        #     elif x == 'R': r += 1
        # return u == d and l == r
