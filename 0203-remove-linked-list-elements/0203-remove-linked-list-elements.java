class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0); // Dummy node to handle edge cases
        dummy.next = head;
        ListNode prev = dummy, curr = head;

        while (curr != null) {
            if (curr.val == val) {
                prev.next = curr.next; // Skip the node
            } else {
                prev = curr; // Move prev forward
            }
            curr = curr.next; // Move curr forward
        }
        return dummy.next;
    }
}
