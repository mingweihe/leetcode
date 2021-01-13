class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
            1 2 3
            4 5 6
            7 8 9
            note: passing through means passing through the center of a key button,
                knight jump is valid
        """
        def backtrack(num_cur, remain):
            if remain == 0: return 1
            ans = 0
            for num_nex in xrange(1, 10):
                if num_nex in seen: continue
                if (num_cur, num_nex) in skip and skip[num_cur, num_nex] not in seen: continue
                seen.add(num_nex)
                ans += backtrack(num_nex, remain-1)
                seen.discard(num_nex)
            return ans
        
        skip = {(1, 3): 2, (3, 1): 2, (1, 7): 4, (7, 1): 4, (7, 9): 8, (9, 7): 8
               ,(3, 9): 6, (9, 3): 6, (1, 9): 5, (9, 1): 5, (3, 7): 5, (7, 3): 5
               ,(2, 8): 5, (8, 2): 5, (4, 6): 5, (6, 4): 5}
        res = 0
        for i in xrange(m, n+1):
            ## optimization
            seen = {1}
            res += backtrack(1, i-1) * 4
            seen = {2}
            res += backtrack(2, i-1) * 4
            seen = {5}
            res += backtrack(5, i-1)
            # for start in xrange(1, 10):
            #     seen = {start}
            #     res += backtrack(start, i-1)
        return res
