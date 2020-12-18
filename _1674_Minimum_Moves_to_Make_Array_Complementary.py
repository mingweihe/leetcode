import collections


class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        one_move_pair_d = collections.defaultdict(int)
        zero_move_pair_d = collections.defaultdict(int)
        n = len(nums)
        for i in xrange(n/2):
            left = nums[i]
            right = nums[n-1-i]
            if left > right: left, right = right, left
            mini, maxi = left+1, limit+right
            one_move_pair_d[mini] += 1
            one_move_pair_d[maxi+1] -= 1
            zero_move_pair_d[left+right] += 1

        num_cur_overlaps, res = 0, n
        for i in xrange(max(one_move_pair_d)+1):
            num_cur_overlaps += one_move_pair_d[i]
            res = min(res, n-num_cur_overlaps-zero_move_pair_d[i])
        return res
