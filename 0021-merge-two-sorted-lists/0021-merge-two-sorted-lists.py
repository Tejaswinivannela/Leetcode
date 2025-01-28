# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Dummy node to simplify handling of the merged list
        dummy = ListNode(-1)
        current = dummy
        
        # Merge the lists while both have remaining nodes
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append the remaining nodes from either list1 or list2
        current.next = list1 if list1 else list2
        
        # Return the merged list starting from the next of the dummy node
        return dummy.next
