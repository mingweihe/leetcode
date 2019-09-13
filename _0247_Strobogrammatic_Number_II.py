class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Approach 2
        def backtracking(m):
            if m == 0: return ['']
            if m == 1: return ['0', '1', '8']
            pre_res = backtracking(m-2)
            res = []
            for s in pre_res:
                if m != n: res.append('0' + s + '0')
                res.append('1' + s + '1')
                res.append('6' + s + '9')
                res.append('8' + s + '8')
                res.append('9' + s + '6')
            return res
        return backtracking(n)

        # Approach 1
        # if n == 0: return ['']
        # d = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        # def backtracking(res, cur, left):
        #     if left == 0:
        #         if str(int(cur)) == cur: res.append(cur)
        #         return
        #     for k, v in d.items():
        #         backtracking(res, k + cur + v, left-1)
        # res = []
        # if n&1:
        #     n = (n-1)/2
        #     backtracking(res, '0', n)
        #     backtracking(res, '1', n)
        #     backtracking(res, '8', n)
        #     return res
        # backtracking(res, '', n / 2)
        # return res
