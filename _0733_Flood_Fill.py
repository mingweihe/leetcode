class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        original_color = image[sr][sc]
        if original_color == newColor: return image
        stack = [(sr,sc)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        h, w = len(image), len(image[0])
        while stack:
            row, col = stack.pop()
            image[row][col] = newColor
            for rm, cm in dirs:
                new_row, new_col = row + rm, col + cm
                if -1 < new_row < h and -1 < new_col < w:
                    if image[new_row][new_col] == original_color:
                        stack.append((new_row, new_col))
        return image
