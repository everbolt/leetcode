# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeKLists(lists):
    tail = head = ListNode()
    i = 0
    while i < len(lists):
        if lists[i] == None:
            lists.pop(i)
            i -= 1
        i += 1
    while len(lists) != 0:
        s_val = 999999999
        s_index = -1
        for i in range(len(lists)):
            if lists[i].val < s_val:
                s_val, s_index = lists[i].val, i
        tail.next = ListNode(s_val)
        tail = tail.next
        lists[s_index] = lists[s_index].next
        if lists[s_index] == None:
            lists.pop(s_index)
    return head.next