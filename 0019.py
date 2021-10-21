# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(head, n):
    if n == 0:
        return head.next
    
    def helper(node, count):
        if count == 0:
            return node.next
        return ListNode(node.val, helper(node.next, count - 1))

    return helper(head, n)