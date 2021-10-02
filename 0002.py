# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def addTwoNumbers(l1, l2):
    tail = head = ListNode()
    over = 0
    while l1 != None or l2 != None:
        l1val, l2val = 0, 0
        if l1 != None:
            l1val, l1 = l1.val, l1.next
        if l2 != None:
            l2val, l2 = l2.val, l2.next
        new = l1val + l2val + over
        over = 1 if new >= 10 else 0
        tail.next = ListNode(new % 10)
        tail = tail.next
    if over:
        tail.next = ListNode(1)
    tail = box = ListNode()
    while head != None:
        tail.next = ListNode(head.val)
        tail, head = tail.next, head.next
    return box.next.next