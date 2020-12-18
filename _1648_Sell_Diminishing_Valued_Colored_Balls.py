class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        MOD = 10**9 + 7
        def check(max_left_order_each):
            res = 0
            for x in inventory:
                if x<= max_left_order_each: continue
                res += x-max_left_order_each
            return res>=orders
        
        l, r = 1, 10**9
        while l < r:
            mid = l + (r-l) / 2
            if check(mid): l = mid + 1
            else: r = mid

        ans = 0
        for x in inventory:
            if x <= l: continue
            cur_order = x-l
            orders -= cur_order
            cost = cur_order * (x+l+1) / 2
            ans += cost
            ans %= MOD
        ans += (l)*orders
        return ans % MOD
