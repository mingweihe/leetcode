class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        res = []
        ip_nb = self.ipToNumber(ip)
        while n:
            emplace_cnt = ip_nb & -ip_nb
            while emplace_cnt > n:
                emplace_cnt >>= 1
            n -= emplace_cnt
            prefix_length = 32 - self.countZeros(emplace_cnt)
            cidr = self.numberToIp(ip_nb) + '/' + str(prefix_length)
            res.append(cidr)
            ip_nb += emplace_cnt
        return res

    def ipToNumber(self, ip):
        nums = list(map(int, ip.split('.')))
        return (nums[0] << 24) + (nums[1] << 16) + (nums[2] << 8) + nums[3]

    def numberToIp(self, nb):
        return '.'.join(map(str, [nb >> 24 & 255, nb >> 16 & 255, nb >> 8 & 255, nb & 255]))

    def countZeros(self, x):
        for i in xrange(32):
            if x & 1 << i:
                return i
