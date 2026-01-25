from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        curr_max = 0
        for i in range(len(nums)//2):
            curr_max = max(curr_max, sorted_nums[i] + sorted_nums[-i-1])
        return curr_max
