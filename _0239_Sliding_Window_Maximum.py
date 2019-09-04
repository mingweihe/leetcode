class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        deque double side operation queue
        deque is for maintaining descending order of qualified
        number array in sliding window
        """
        if not nums: return []
        L, deque = len(nums), []
        res = [0]*(L-k+1)
        for i,x in enumerate(nums):
            if deque and deque[0] == i-k: deque.pop(0)
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            if i-k > -2: res[i-k+1] = nums[deque[0]]
        return res
