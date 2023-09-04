# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyds Tortoise and Hare algorithm 
        fast, slow = head, head 
        i = 0 
        while fast and fast.next: 
            print(f'iteration {i}')
            fast = fast.next.next
            slow = slow.next
            i += 1
            if fast == slow: 
                return True 
                        
        return False 
    
if __name__ == "__main__":
    print(Solution().hasCycle(ListNode(1, ListNode(2))))
    