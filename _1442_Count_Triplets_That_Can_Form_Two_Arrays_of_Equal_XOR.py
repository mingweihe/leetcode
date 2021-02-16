class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ## Approach 3, O(n)
        res = cur = 0
        count = {0: [1, 0]}
        for i, x in enumerate(arr):
            cur ^= x
            n, total = count.get(cur, [0, 0])
            res += i * n - total
            count[cur] = [n+1, total+i+1]
        return res

        ## Approach 2, O(n^2)
        # res, pre = 0, [0]
        # for x in arr: pre += pre[-1] ^ x,
        # for i in xrange(len(pre)-1):
        #     for k in xrange(i+1, len(pre)):
        #         if pre[i] == pre[k]:
        #             res += k - i - 1
        # return res
        
        ## Approach 1, O(n^3)
        # res, pre = 0, [0]
        # for x in arr:
        #     pre += pre[-1] ^ x,
        # for i in xrange(len(arr)-1):
        #     for j in xrange(i+1, len(arr)):
        #         for k in xrange(j, len(arr)):
        #             a = pre[j] ^ pre[i]
        #             b = pre[k+1] ^ pre[j]
        #             res += a == b
        # return res
