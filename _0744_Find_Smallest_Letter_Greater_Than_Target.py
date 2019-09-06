import bisect


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # Approach 2
        pos = bisect.bisect_right(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]

        # Approach 1
        # for c in letters:
        #     if c > target: return c
        # return letters[0]
