class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        # Approach 1
        setA, setB = set(A), set(B)
        if setB.issubset(setA):
            lA = len(A)
            lB = len(B)
            if lA < lB:
                times = lB / lA
                for i in range(times, times + 3):
                    if B in A * i: return i
                return -1
            else:
                for times in range(1, 3):
                    if B in A * times: return times
                return -1
        return -1
        # Approach 2
        # cnt = 0
        # times = len(B) // len(A)
        # de_times = len(B) / len(A)
        # if times == de_times:
        #     cnt = times
        #     s = A * times
        # else:
        #     cnt = times + 1
        #     s = A * (times + 1)
        # if B in s:
        #     return cnt
        # elif B in s + A:
        #     return cnt + 1
        # return -1
