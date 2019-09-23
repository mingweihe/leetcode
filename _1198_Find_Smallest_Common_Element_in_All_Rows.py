class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # Approach 2
        s = set(mat[0])
        for row in mat:
            s = s.intersection(row)
        if s: return min(s)
        return -1

        # Approach 1
        # m, n = len(mat), len(mat[0])
        # for j in xrange(n):
        #     num, cnt = mat[0][j], 0
        #     for i in xrange(m):
        #         idx = bisect.bisect_left(mat[i], num)
        #         if idx!= n and mat[i][idx] == num: cnt += 1
        #     if cnt == m: return num
        # return -1
