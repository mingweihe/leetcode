class Solution(object):
    def longestSubsequence(self, arr, diff):
        """
        :type arr: List[int]
        :type diff: int
        :rtype: int
            trick and principle, algorithms of calculating result set and number
            of result set are not same, the latter is usually easier
        """
        dic = dict()
        for num in arr:
            dic[num] = dic.get(num-diff, 0) + 1
        return max(dic.values())
