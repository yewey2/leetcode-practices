from typing import List, Optional


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # start 10.23
        def to_bin(x):
            return str(bin(x))[2:]

        def to_dec(x):
            return int(x, 2)

        s = '0'
        for i in range(1, n + 1):
            s += to_bin(i)
        return to_dec(s) % (10**9 + 7)
        # done 10.27