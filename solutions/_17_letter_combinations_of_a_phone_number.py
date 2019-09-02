class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        if not digits: return res
        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', \
               '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def dfs(cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for x in dic[digits[len(cur)]]:
                dfs(cur + x)
        dfs('')
        return res
