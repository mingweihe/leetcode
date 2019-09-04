class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        # Approach 1
        H, W = len(M), len(M[0])
        m = [[0] * W for _ in xrange(H)]
        dirs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for i in xrange(H):
            for j in xrange(W):
                S, cnt = 0, 0
                for k, l in dirs:
                    x, y = i + k, j + l
                    if x in (-1, H) or y in (-1, W): continue
                    S += M[x][y]
                    cnt += 1
                m[i][j] = S // cnt
        return m
        # Approach 2
        # H, W = len(M), len(M[0])
        # m = np.copy(M)
        # for i in range(len(M)):
        #     for j in range(len(M[0])):
        #         L_index = j - 1 if j > 0 else j
        #         R_index = j + 2 if j < W - 1 else j + 1
        #         U_index = i - 1 if i > 0 else i
        #         D_index = i + 2 if i < H - 1 else i + 1
        #         M[i][j] = int(np.average(m[U_index:D_index, L_index:R_index]))
        # return M
