# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 , stack2 = [], [] 
        
        while l1: 
            stack1.append(l1.val)
            l1 = l1.next
        while l2: 
            stack2.append(l2.val)
            l2 = l2.next

        total, carry = 0, 0
        current = None
        
        while stack1 or stack2: 
            total = carry
            total = total  + ( stack1.pop() if stack1 else 0 )
            total = total  + ( stack2.pop() if stack2 else 0 )
            
            carry = total//10 
            val = total%10

            node = ListNode(val)
            node.next = current
            current = node 

        if carry > 0: 
            node = ListNode(carry)
            node.next = current 
            current = node 
        
        return current 
        

if __name__ == "__main__":
    s = Solution() 
    l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    print(s.addTwoNumbers(l1, l2))