class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null) {
            ListNode next = curr.next;  // Store next node
            curr.next = prev;           // Reverse link
            prev = curr;                // Move prev forward
            curr = next;                // Move curr forward
        }
        return prev;  // New head of reversed list
    }
}
