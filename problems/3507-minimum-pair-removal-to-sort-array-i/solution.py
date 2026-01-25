from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ## do you need to find minimum pair sum? probably not
        ## go through left to right
        # curr = 0
        # prev = 0
        # total = 0
        # for i in range(len(nums)):
        #     prev = max(nums[i], curr)
        #     curr = max(curr, nums[i])
        #     if curr < prev:  
        #         total += 1
        # return total

        ## start from last
        # if not nums: return 0
        # counter = 0
        # rnums = nums[::-1]
        # while len(rnums) > 1:
        #     if rnums[0] < rnums[1]:
        #         rnums[1] = rnums[0] + rnums[1]
        #         counter += 1
        #     rnums.pop(0)
        # return counter
        ## brute force first
        def func(nums, ops):
            ## check sorted
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    break
            else:
                return ops
            sum_pairs = [nums[i]+nums[i+1] for i in range(len(nums)-1)]
            m = min(sum_pairs)
            ind = sum_pairs.index(m)
            nums[ind] = m
            nums.pop(ind+1)
            return func(nums, ops+1)
        return func(nums, 0)
