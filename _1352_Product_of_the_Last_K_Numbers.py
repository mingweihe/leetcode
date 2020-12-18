class ProductOfNumbers(object):

    def __init__(self):
        self.A = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0: self.A = [1]
        else: self.A += self.A[-1] * num,
        
    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.A): return 0
        return self.A[-1] / self.A[-k-1]
            

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
