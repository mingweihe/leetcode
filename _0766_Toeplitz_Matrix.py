class Solution(object):
    def isToeplitzMatrix(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # Approach 3
        return all(m[row + 1][1:] == m[row][:-1] for row in range(len(m) - 1))

        # Approach 2
        # return all(m[i][j]==m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))

        # Approach 1
        # w, h = len(m[0]), len(m)
        # for i in range(h):
        #     for j in range(w):
        #         if i+1<h and j+1<w and m[i][j] != m[i+1][j+1]:
        #             return False
        # return True
