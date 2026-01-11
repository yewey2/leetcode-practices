## imports so that pylance doesn't complain 
from typing import Optional

## Actual code
## ----------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    ## My solution - newest improved based on gemini suggestions
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            vnew = v1+v2+carry
            m1 = l1.next if l1 else None
            m2 = l2.next if l2 else None
            carry = 1 if vnew >= 10 else 0
            vnew -=10 if vnew >=10 else 0
            
            return ListNode(vnew, add(m1, m2, carry))
        return add(l1, l2, 0)
#     ## gemini solution - for reference
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         curr = dummy
#         carry = 0
        
#         # Keep going as long as there are digits OR a remaining carry
#         while l1 or l2 or carry:
#             # Get values, defaulting to 0 if the list has ended
#             val1 = l1.val if l1 else 0
#             val2 = l2.val if l2 else 0
            
#             # Calculate sum and carry
#             total = val1 + val2 + carry
#             carry = total // 10
#             new_val = total % 10
            
#             # Create new node and move pointer
#             curr.next = ListNode(new_val)
#             curr = curr.next
            
#             # Move to next nodes in input lists if they exist
#             if l1: l1 = l1.next
#             if l2: l2 = l2.next
            
#         return dummy.next

    ## my solution (original)
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     ## base case
    #     if l1 is None and l2 is None:
    #         return None
    #     if l1 is None or (l1.val == 0 and l1.next is None):
    #         return l2
    #     if l2 is None or (l2.val == 0 and l2.next is None):
    #         return l1

    #     def handleTens(l):
    #         if l.val < 10:
    #             return l
    #         if l.next is None:
    #             return ListNode(l.val-10, ListNode(1))
    #         l.next.val+=1
    #         return ListNode(l.val-10, handleTens(l.next))

    #     ## case for l1 + l2 < 10        
    #     if l1.val + l2.val < 10:
    #         return ListNode(l1.val+l2.val, self.addTwoNumbers(l1.next, l2.next))
    #     ## case for l1 + l2 >= 10
    #     ## case for both l1 and l2 is None
    #     if l1.next is None and l2.next is None:
    #         return ListNode(l1.val+l2.val-10, ListNode(1, None))
    #     ### case for l1 has nothing
    #     if l1.next is None:
    #         l2.next.val += 1
    #         return ListNode(l1.val+l2.val-10, handleTens(l2.next))
    #     ### case for l2 has nothing
    #     if l2.next is None:
    #         l1.next.val += 1
    #         return ListNode(l1.val+l2.val-10, handleTens(l1.next))
    #     ## case for both l1 and l2 exists, just select l1
    #     l1.next.val +=1
    #     return ListNode(l1.val+l2.val-10, (self.addTwoNumbers(handleTens(l1.next), l2.next)))
