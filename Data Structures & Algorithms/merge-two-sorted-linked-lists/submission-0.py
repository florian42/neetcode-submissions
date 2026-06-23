# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2
        if list2 is None and list1 is not None:
            return list1
        if list1 is None and list2 is None:
            return None

        
        curr1 = list1
        curr2 = list2
        new_head = None
        if list1.val <= list2.val:
            new_head = list1
            curr1 = list1.next
        else:
            new_head = list2
            curr2 = list2.next

        tail = new_head
        

        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                tail = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                tail = curr2
                curr2 = curr2.next

        while curr1:
            tail.next = curr1
            tail = tail.next
            curr1 = curr1.next

        while curr2:
            tail.next = curr2
            tail = tail.next
            curr2 = curr2.next

        return new_head

            
        