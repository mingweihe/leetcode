class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # Approach 2
        return [x for x in range(left, right + 1) if all(i and x % i == 0 for i in map(int, str(x)))]

        # Approach 1
        # res = []
        # for x in range(left, right + 1):
        #     cur = x
        #     while cur:
        #         digit = cur % 10
        #         if digit == 0 or x % digit != 0:
        #             break
        #         cur //= 10
        #     if cur == 0:
        #         res.append(x)
        # return res
