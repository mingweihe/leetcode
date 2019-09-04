class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Approach 2
        S = [1, 2, 2]
        idx = 2
        while len(S) < n:
            S += S[idx] * [(3 - S[-1])]
            idx += 1
        return S[:n].count(1)
        
        # Approach 1
        # if n in (1,2): return 1
        # j, cur = 3, '122'
        # while True:
        #     t='1'
        #     for i in range(1,j):
        #         if cur[i] == '2':
        #             if t[-1] == '1': t+='22'
        #             else: t+='11'
        #         else:
        #             if t[-1] == '1': t+='2'
        #             else: t+='1'
        #     if len(t) >= n: return t[:n].count('1')
        #     j, cur = len(t), t
