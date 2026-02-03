from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        ## 9.54am
        # if len(nums) <= 3: 
        #     return False
        # curr = nums[0]image.png
        # parity = 0
        # if nums[0] >= nums[1]: 
        #     return False
        # for i in nums[1:-1]:
        #     if curr == i: return False
        #     print(curr, i, parity)
        #     if parity == 0:
        #         if curr < i:
        #             curr = i
        #             continue
        #         parity = 1
        #         curr = i
        #         continue
        #     if parity == 1:
        #         curr = i
        #         if curr > i:
        #             curr = i
        #             continue
        #         parity = 2
        #         curr = i
        #         continue
        #     if parity == 2:
        #         if curr < i:
        #             curr = i
        #             continue
        #         return False
        # return parity == 2 and nums[-1] > curr
        ## stopped 9.59
        ## bad method. retry 
        ## strat 2.40pm
        curr = nums[0]
        positive = True
        count = 0
        if nums[0] >= nums[1]: return False
        if nums[-1] < nums[-2]: return False
        for i in nums[1:]:
            print(curr, positive, count)
            if i == curr: 
                return False
            if positive and i < curr:
                count += 1
                positive = not positive
            if not positive and i > curr:
                count += 1
                positive = not positive
            if count >3: 
                return False
            curr = i
            print('now', curr, positive, count)
        return count==2
        ## complete 2.47
