class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # Approach 3
        return sum(665772 >> bin(x).count('1') & 1 for x in range(L, R + 1))

        # Approach 2
        # primes = {2, 3, 5, 7, 11, 13, 17, 19}
        # return len([x for x in range(L, R+1) if bin(x).count('1') in primes])

        # Approach 1
        # primes = {}
        # res = 0
        # for x in range(L, R+1):
        #     num_bits = bin(x).count('1')
        #     if num_bits == 1:
        #         continue
        #     if primes.get(num_bits):
        #         res += 1
        #         continue
        #     is_prime = True
        #     for i in range(2, int(num_bits**.5)+1):
        #         if num_bits % i == 0:
        #             is_prime = False
        #             break
        #     if is_prime:
        #         primes[num_bits] = True
        #         res += 1
        # return res
