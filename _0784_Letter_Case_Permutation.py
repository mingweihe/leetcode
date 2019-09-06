class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        # Approach 4: iteration
        res = ['']
        for c in S:
            if c.isalpha():
                res = [i+j for i in res for j in (c.upper(), c.lower())]
            else:
                res = [i+c for i in res]
        return res

        # Approach 3: recursion
        # if not S: return ['']
        # c = S[0]
        # sub_set = self.letterCasePermutation(S[1:])
        # if '0'<=c<='9':
        #     return [c+x for x in sub_set]
        # else:
        #     return [c.upper()+x for x in sub_set] + [c.lower()+x for x in sub_set]

        # Approach 2
        # L = [[i.upper(), i.lower()] if i.isalpha() else i for i in S]
        # return list(map(''.join, itertools.product(*L)))

        # Approach 1
        # res = []
        # s_arr = list(S.lower())
        # pos = [i for i,x in enumerate(s_arr) if x.isalpha()]
        # L = len(pos)
        # if L == 0: return [S]
        # for i in range(pow(2, L)):
        #     for i,x in enumerate(bin(i)[2:][::-1]):
        #         if x == '1':
        #             s_arr[pos[L-i-1]] = s_arr[pos[L-i-1]].upper()
        #         else:
        #             s_arr[pos[L-i-1]] = s_arr[pos[L-i-1]].lower()
        #     res.append(''.join(s_arr))
        # return res
