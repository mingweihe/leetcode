class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # Approach 3 set reduce
        # set.__and__ is same with operator.add_
        s = reduce(set.__and__, [set(pair) for pair in zip(A, B)])
        if not s: return -1
        num = s.pop()
        return min(len(A)-A.count(num), len(B)-B.count(num))

        # Approach 2 check A[0] and B[0]
        # res, L = float('inf'), len(A)
        # for i in (A[0], B[0]):
        #     cnt_a = cnt_b = 0
        #     for j in xrange(L):
        #         if A[j] != i and B[j] != i:
        #             cnt_a = -1
        #             break
        #         if A[j] != i: cnt_a += 1
        #         if B[j] != i: cnt_b += 1
        #     if cnt_a == -1: continue
        #     res = min(res, cnt_a, cnt_b)
        # return -1 if res == float('inf') else res
        
        # Approach 1 check 1 to 7
        # res, L = float('inf'), len(A)
        # for i in xrange(1, 7):
        #     cnt_a = cnt_b = 0
        #     for j in xrange(L):
        #         if A[j] != i and B[j] != i:
        #             cnt_a = -1
        #             break
        #         if A[j] != i: cnt_a += 1
        #         if B[j] != i: cnt_b += 1
        #     if cnt_a == -1: continue
        #     res = min(res, cnt_a, cnt_b)
        # return -1 if res == float('inf') else res
