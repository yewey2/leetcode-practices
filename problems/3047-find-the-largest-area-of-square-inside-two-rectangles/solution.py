from typing import List
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ## idea 1: brute force
        squares = list(zip(bottomLeft, topRight))
        max_area = 0
        for i, s1 in enumerate(squares):
            for j, s2 in enumerate(squares[i+1:], i+1):
                ## compare two squares
                s1bl, s1tr = s1
                s2bl, s2tr = s2
                s1b, s1l = s1bl
                s1t, s1r = s1tr
                s2b, s2l = s2bl
                s2t, s2r = s2tr
                ## compare s1b and s1t to s2b s2t
                height = max(min(s2t, s1t) - max(s1b, s2b), 0)
                width = max(min(s2r, s1r) - max(s1l, s2l), 0)
                size = min(width, height)
                area = size * size
                max_area = max(area, max_area)
        return max_area
