class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int

        """
        # Approach 2 faster pow + matrix multiplication time O(log(n))
        M = 10 ** 9 + 7

        def matmul(A, B):
            m, n, x = len(A), len(B[0]), len(B)
            C = [[0] * n for _ in xrange(m)]
            for i in xrange(m):
                for j in xrange(n):
                    for k in xrange(x):
                        C[i][j] += A[i][k] * B[k][j]
                    C[i][j] %= M
            return C

        transition_matrix = [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0]
        ]
        ans = [[1], [1], [1], [1], [1]]
        n -= 1
        while n:
            if n & 1: ans = matmul(transition_matrix, ans)
            n >>= 1
            transition_matrix = matmul(transition_matrix, transition_matrix)
        return sum(map(sum, ans)) % M

        # Approach 1 five variables time O(n)
        # M = 10**9+7
        # a = e = i = o = u = 1
        # for _ in xrange(n-1):
        #     a1 = (e + i + u) % M
        #     e1 = (a + i) % M
        #     i1 = (e + o) % M
        #     o1 = i % M
        #     u1 = (i + o) % M
        #     a, e, i, o, u = a1, e1, i1, o1, u1
        # return (a+e+i+o+u) % M
