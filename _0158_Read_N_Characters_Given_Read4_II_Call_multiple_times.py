"""
The read4 API is already defined for you.
    def read4(buf): @param buf, a list of characters, @return an integer
# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""


def read4(buf):
    return 0


class Solution(object):
    def __init__(self):
        self.count = self.pointer = 0
        self.temp = [''] * 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        index = 0
        while index < n:
            if self.pointer == 0:
                self.count = read4(self.temp)
            if self.count == 0: break
            while index < n and self.pointer < self.count:
                buf[index] = self.temp[self.pointer]
                index += 1
                self.pointer += 1
            if self.pointer == self.count:
                self.pointer = 0
        return index
