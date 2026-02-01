from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # start 732pm
        ## idea is: sort and get the 3 lowest subarrays.
        # return sum(sorted(nums)[:3])
        ## this doesn't work because it's the START. so the first one must be included
        ## next idea, sort, but exclude first one (index 0)
        return nums[0] + sum(sorted(nums[1:])[:2])
        ## solved 734
