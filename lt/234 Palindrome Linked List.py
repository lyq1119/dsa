class Solution:
    def isPalindrome(self, head) -> bool:
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = ListNode(slow.val,prev)
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True
