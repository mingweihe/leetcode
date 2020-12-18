class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.forward_hist = []
        self.back_hist = []
        self.cur_page = homepage
        
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.forward_hist = []
        self.back_hist += self.cur_page,
        self.cur_page = url

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        x = len(self.back_hist)
        steps = min(steps, x)
        for i in xrange(steps):
            self.forward_hist += self.cur_page,
            self.cur_page = self.back_hist.pop()
        return self.cur_page
            
    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        x = len(self.forward_hist)
        steps = min(steps, x)
        for i in xrange(steps):
            self.back_hist += self.cur_page,
            self.cur_page = self.forward_hist.pop()
        return self.cur_page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
