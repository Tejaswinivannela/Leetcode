# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify edge cases (e.g., removing the head)
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move the fast pointer n+1 steps ahead to maintain a gap of n nodes
        for _ in range(n + 1):
            fast = fast.next

        # Move both slow and fast pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        # Return the head of the updated list
        return dummy.next
