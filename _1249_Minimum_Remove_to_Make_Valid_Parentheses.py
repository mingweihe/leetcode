class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """

        def helper(sss, valid_p, check_p):
            ans = []
            cnt = 0
            for c in sss:
                if c.isalpha():
                    ans += c
                elif c == valid_p:
                    cnt += 1
                    ans += valid_p,
                else:
                    if cnt > 0:
                        ans += check_p,
                        cnt -= 1
            return ''.join(ans)

        res = helper(s, '(', ')')
        res = helper(res[::-1], ')', '(')
        return res[::-1]
