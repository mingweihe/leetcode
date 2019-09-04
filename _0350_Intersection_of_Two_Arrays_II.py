import collections


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Approach 2
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
        # Approach 1
        # d, res={}, []
        # for i in nums1:
        #     d[i] = 1 if not i in d else d[i] + 1
        # for i in nums2:
        #     if i in d and d[i] > 0:
        #         res.append(i)
        #         d[i] -= 1
        # return res
