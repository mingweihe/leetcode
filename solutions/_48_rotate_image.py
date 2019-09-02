class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        rotate == flip along diagonal + flip along horizontal/vertical symmetrical axis
        """
        L = len(matrix)
        for i in xrange(L):
            for j in xrange(i, L):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in xrange(L):
            for j in xrange(0, L / 2):
                matrix[i][j], matrix[i][L - 1 - j] = matrix[i][L - 1 - j], matrix[i][j]
