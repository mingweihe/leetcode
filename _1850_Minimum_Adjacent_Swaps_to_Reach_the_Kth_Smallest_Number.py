class Solution(object):
    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """
        def nextPermutation(nums):
            N, first_smaller = len(nums), -1
            for i in xrange(N-2, -1, -1):
                if nums[i] < nums[i+1]:
                    first_smaller = i
                    break
            if first_smaller == -1: 
                nums.reverse()
                return
            for i in xrange(N-1, first_smaller, -1):
                if nums[i] > nums[first_smaller]:
                    nums[i], nums[first_smaller] = nums[first_smaller], nums[i]
                    break
            l, r = first_smaller + 1, N - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        A = list(num)
        for _ in xrange(k):
            nextPermutation(A)
        def get_swaps(arr1, arr2):
            ans = 0
            for i, x in enumerate(arr1):
                if x == arr2[i]: continue
                idx = i + 1
                while arr2[idx] != x:
                    idx += 1
                for j in xrange(idx, i, -1):
                    arr2[j], arr2[j-1] = arr2[j-1], arr2[j]
                    ans += 1
            return ans
        return get_swaps(list(num), A)
