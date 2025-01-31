class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip duplicate node
            else:
                current = current.next  # Move to the next node
        
        return head  # Return modified linked list

# Helper function to create a linked list from a list
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)

# Example usage
head = create_linked_list([1, 1, 2, 3, 3])
solution = Solution()  # Create an instance of Solution
new_head = solution.deleteDuplicates(head)
print_linked_list(new_head)  # Output: [1, 2, 3]
