class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # Approach 2 reuse input array, time O(n), space O(1)
        i, mini = 0, -float('inf')
        for x in preorder:
            if x < mini: return False
            while i > 0 and x > preorder[i - 1]:
                i -= 1
                mini = preorder[i]
            preorder[i] = x
            i += 1
        return True

        # Approach 1 stack time O(n) space O(n)
        # stack, mini = [], float('-inf')
        # for x in preorder:
        #     if x < mini: return False
        #     while stack and x > stack[-1]:
        #         mini = stack.pop()
        #     stack.append(x)
        # return True
