class Solution(object):
    def parseTernary(self, exp):
        """
        :type exp: str
        :rtype: str
        """
        # Approach 2 stack time O(n)
        stack = []
        for i in xrange(len(exp)-1, -1, -1):
            if stack and stack[-1] == '?':
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()
                if exp[i] == 'T': stack.append(first)
                else: stack.append(second)
            else: stack.append(exp[i])
        return stack[-1]

        # Approach 1 dfs worst time complexity O(n^2)
        # def dfs(start, end):
        #     if start == end: return exp[start]
        #     cnt = 0
        #     for i in xrange(start+1, end+1):
        #         if exp[i] == '?': cnt += 1
        #         elif exp[i] == ':':
        #             cnt -= 1
        #             if cnt == 0: break
        #     if exp[start] == 'T':
        #         return dfs(start+2, i-1)
        #     else:
        #         return dfs(i+1, end)
        # return dfs(0, len(exp)-1)
