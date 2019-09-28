class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # Approach 2 time O(n) space O(1)
        L1, L2 = len(S), len(T)
        i, j, cnt1, cnt2 = L1-1, L2-1, 0, 0
        while i >= 0 or j >= 0:
            while i >= 0 and (S[i] == '#' or cnt1 > 0):
                if S[i] == '#':
                    cnt1 += 1
                else:
                    cnt1 -= 1
                i -= 1
            while j >= 0 and (T[j] == '#' or cnt2 > 0):
                if T[j] == '#':
                    cnt2 += 1
                else:
                    cnt2 -= 1
                j -= 1
            if i >= 0 and j >= 0 and S[i] == T[j]:
                    i -= 1
                    j -= 1
            else: return i == j == -1
        return True

        # Approach 1 time O(n) space O(n)
        # convert = lambda res, c: res[:-1] if c == '#' else res + c
        # return reduce(convert, S, '') == reduce(convert, T, '')
