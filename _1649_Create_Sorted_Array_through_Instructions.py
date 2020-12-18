from sortedcontainers import SortedSet
class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        ## approach 2 fenwick tree / binary index tree
        MOD = 10**9 + 7 
        A = [0] * (max(instructions) + 1)
        def update(x):
            while x < len(A):
                A[x] += 1
                # x + lowbit
                x += x & -x
        
        def query(x):
            res = 0
            while x > 0:
                res += A[x]
                x -= x & -x
            return res
        
        ans = 0
        for i, a in enumerate(instructions):
            ans += min(query(a-1), i-query(a))
            ans %= MOD
            update(a)
        
        return ans

        ## approach 1 bisect
        # nums = []
        # MOD = 10**9 + 7
        # cost = 0
        # for x in instructions:
        #     num_less = bisect_left(nums, x)
        #     num_greater = len(nums) - bisect_right(nums, x)
        #     cost += min(num_less, num_greater)
        #     insort(nums, x)
        #     cost %= MOD
        # return cost
