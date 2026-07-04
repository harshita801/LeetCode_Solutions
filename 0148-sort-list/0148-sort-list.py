# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()

        temp=head
        for value in arr:
            temp.val=value
            temp=temp.next
        return head
