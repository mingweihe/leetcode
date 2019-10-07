class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
            one more time, it's important to clearly explain and understand
            the meaning of the puzzle!!!
        """
        # Approach 2 DFS
        res = set()

        def search(x):
            if x > high: return
            if x >= low: res.add(x)
            last = x % 10
            if last > 0: search(x * 10 + last - 1)
            if last < 9: search(x * 10 + last + 1)

        for i in xrange(10): search(i)
        return sorted(res)

        # Approach 1 BFS
        # dq = collections.deque()
        # for i in xrange(1, 10): dq.append(i)
        # res = []
        # if low == 0: res.append(0)
        # while dq:
        #     num = dq.popleft()
        #     if low <= num <= high: res.append(num)
        #     if num < high:
        #         last = num % 10
        #         if last > 0: dq.append(num * 10 + last - 1)
        #         if last < 9: dq.append(num * 10 + last + 1)
        # return res
