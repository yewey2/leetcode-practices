class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        ## start 8pm
        ## notes: 2^i + num2 is just finding a series of N(i)s + N(num2) to make num1
        ## brute force method would be to list out the full i=60. 

        # if num1 < 1 or num1 - num2 < 0
        if num1 == 0 : return 0
        ## stopped at 8.12pm 
        ## see solution
        # for k in range(1, 61):
        #     x = num1 - num2 * k
        #     print(x)
        #     if x < k:
        #         return -1
        #     if k >= x.bit_count():
        #         print('k is', k, 'bit count is', x.bit_count())
        #         return k
        # return -1

        ## continue at 10.19 by myself without solution
        ## logic: 
        ## N (num 2) + N(2^i) = num 1
        ## by algebraic manipulation
        ## num1 - N(num2) = N(2^i)
        ## create a helper function first for bit count, aka how many pwoer of 2s there are inside a number, i.e. binary representation
        def binary(x):
            return 
        ## we can check brute force for all 60, whether there exists a N for num1 - N(num2) is a sum of 2^i
        for i in range(61):
            lhs = num1 - num2*i
            if lhs < i:
                continue
            ## now if lhs can be represented by powers of 2, and we have mroe than enough i, then we're good
            if i >= lhs.bit_count():
                return i
        return -1
        ## complete: 10.32
