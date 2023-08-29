# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        c = 0
        while l1 or l2 or c: 
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0 ) + c
            c = (s//10)
            current.next = ListNode(s%10)
            current = current.next
            l1 = l1.next if l1 else 0 
            l2 = l2.next if l2 else 0
        return head.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(5, ListNode(6, ListNode(4)))
    l2 = ListNode(7, ListNode(0, ListNode(8)))
    result = s.addTwoNumbers(l1, l2)
    while result:
        delim = " -> "  if result.next else ""
        print(result.val, end= delim)
        result = result.next

