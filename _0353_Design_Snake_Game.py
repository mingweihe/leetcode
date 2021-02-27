from collections import deque


dirs = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.i = self.j = 0
        self.w, self.h = width, height
        self.food = food
        self.score = 0
        self.body = deque([[0, 0]])

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        di, dj = dirs[direction]
        self.i, self.j = self.i + di, self.j + dj
        if self.i < 0 or self.i == self.h or self.j < 0 or self.j == self.w:
            return -1
        if self.score < len(self.food) and [self.i, self.j] == self.food[self.score]:
            self.score += 1
            self.body.appendleft([self.i, self.j])
            return self.score
        self.body.pop()
        for body_i in self.body:
            if body_i == [self.i, self.j]: return -1
        self.body.appendleft([self.i, self.j])
        return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
