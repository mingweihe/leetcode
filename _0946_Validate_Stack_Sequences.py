class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        ## Approach 3, utilize the pushed array, O(1) space complexity
        i, j = 0, 0
        for x in pushed:
            pushed[i] = x
            while i >= 0 and pushed[i] == popped[j]:
                i, j = i-1, j+1
            i += 1
        return i == 0
        
        ## Approach 2, simulating the push pop operation using an stack
        # stack, i = [], 0
        # for x in pushed:
        #     stack.append(x)
        #     while stack and stack[-1] == popped[i]:
        #         stack.pop()
        #         i += 1
        # return len(stack) == 0
        
        ## Approach 1
        # pushed, popped = pushed[::-1], popped[::-1]
        # stack = []
        # while popped:
        #     while pushed and (not stack or popped and stack[-1] != popped[-1]):
        #         stack.append(pushed.pop())
        #     if stack and stack[-1] != popped[-1]: return False
        #     while popped and stack and popped[-1] == stack[-1]:
        #         stack.pop()
        #         popped.pop()
        # return True
