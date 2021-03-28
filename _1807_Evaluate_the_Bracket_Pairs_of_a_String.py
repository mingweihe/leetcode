class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        d = {k: v for k, v in knowledge}
        num_brackets = 0
        ans, cur = '', ''
        for x in s:
            if x == ')':
                if cur in d: ans += d[cur]
                else: ans += '?'
                cur = ''
                num_brackets -= 1
            elif x == '(':
                num_brackets += 1
            else:
                if num_brackets == 0:
                    ans += x
                else:
                    cur += x
        return ans
