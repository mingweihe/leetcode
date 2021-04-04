class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        ## Approach 1, O(n*log(n))
        st = set(nums)
        maxi, ans = max(st), 0
        for x in xrange(1, maxi+1):
            cur = 0
            for y in xrange(x, maxi+1, x):
                if y not in st: continue
                cur = gcd(cur, y)
                if cur == x:
                    ans += 1
                    break
        return ans
        
        ## Approach 1, O(n*sqrt(n)), TLE
        # maxi = max(nums)
        # gcds = [0] * (maxi + 1)
        # for x in nums:
        #     for i in xrange(1, int(x**.5)+1):
        #         if x % i: continue
        #         gcds[i] = gcd(gcds[i], x)
        #         gcds[x/i] = gcd(gcds[x/i], x)
        # ans = 0
        # for i in xrange(1, maxi + 1):
        #     ans += gcds[i] == i
        # return ans
