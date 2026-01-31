from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ## Old code from long ago
        # s = sorted(filter(lambda x: x > ord(target), map(lambda x: ord(x), letters)))
        # if s:
        #     return chr(s[0])
        # return letters[0]
        #
        ## Start 7.56pm
        ## note: letters are already sorted
        for l in letters:
            if l > target: 
                return l
        return letters[0]
        ## complete 7.57pm
