class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Approach 3
        return ['FizzBuzz'[i % -3 & -4:i % -5 & 8 ^ 12] or `i` for i in xrange(1, n + 1)]

        # Approach 2
        # return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or `i` for i in xrange(1, n+1)]

        # Approach 1
        # return ['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 \
        #         else 'Buzz' if i%5==0 else `i` for i in xrange(1,n+1)]
