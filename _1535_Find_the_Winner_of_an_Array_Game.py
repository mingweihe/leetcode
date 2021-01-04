class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        ## Approach 2
        cnt = 0
        cur = arr[0]
        for x in arr[1:]:
            if cur < x:
                cur = x
                cnt = 0
            cnt += 1
            if cnt == k: break
        return cur
            
        ## Apparoch 1
        # if k >= len(arr): return max(arr)
        # dq = deque(arr)
        # cnt = 0
        # cur = dq.popleft()
        # while cnt != k:
        #     if cur > dq[0]:
        #         cnt += 1
        #         dq.append(dq.popleft())
        #     else:
        #         cnt = 1
        #         dq.append(cur)
        #         cur = dq.popleft()
        # return cur
