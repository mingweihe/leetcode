class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        numsSort = sorted(nums)
        d = {}
        L = len(nums)
        top3 = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(L):
            if L-i < 4: d[numsSort[i]] = top3[L-i-1]
            else: d[numsSort[i]] = str(L-i)
        for i in range(L): nums[i] = d[nums[i]]
        return nums
