class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Approach 2
        if not nums:
            return [-1, -1]

        def search(lo, hi):
            if nums[lo] == target == nums[hi]: return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo+hi) / 2
                l = search(lo, mid)
                r = search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)

        # Approach 1
        # res = [-1, -1]
        # if not nums: return res
        # def binarySearch(objective):
        #     left, right = 0, len(nums)-1
        #     while left <= right:
        #         mid = (left+right) / 2
        #         if nums[mid] < objective:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     return left
        # start = binarySearch(target-0.5)
        # end = binarySearch(target+0.5)
        # if end - start == 0: return res
        # return [start, end-1]
