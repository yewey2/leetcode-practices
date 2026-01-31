class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        ## start 7.58pm
        d1 = abs(z-x)
        d2 = abs(z-y)
        return 1 if d1<d2 else 2 if d2<d1 else 0
        ## done 7.59pm
