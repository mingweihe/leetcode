class Solution(object):
    def countSquares(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # Approach 2, DP
        res = 0
        for i in xrange(len(M)):
            for j in xrange(len(M[0])):
                if M[i][j] == 1:
                    if i - 1 >= 0 and j - 1 >= 0:
                        M[i][j] += min(M[i - 1][j], M[i][j - 1], M[i - 1][j - 1])
                    res += M[i][j]
        return res

        # Approach 1, BFS
        # res = 0
        # for i in xrange(len(M)):
        #     for j in xrange(len(M[0])):
        #         if M[i][j] == 1:
        #             bottom, right = i, j
        #             res += 1
        #             ii, jj = i-1, j-1
        #             flag = True
        #             while flag:
        #                 if ii < 0 or jj < 0 or M[ii][jj] == 0: break
        #                 for x in xrange(ii+1, bottom+1):
        #                     if M[x][jj] == 0:
        #                         flag = False
        #                         break
        #                 for y in xrange(jj+1, right+1):
        #                     if M[ii][y] == 0:
        #                         flag = False
        #                         break
        #                 if flag: res += 1
        #                 ii, jj = ii-1, jj-1
        # return res
