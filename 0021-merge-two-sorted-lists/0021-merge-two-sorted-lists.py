# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if(not list1 and not list2):
            return None
        if(not list1 and list2):
            return list2
        if(list1 and not list2):
            return list1
        
        curr1 = list1
        curr2 = list2

        if(curr1.val <= curr2.val):
            new_list = ListNode(curr1.val)
            curr1 = curr1.next
        else:
            new_list = ListNode(curr2.val)
            curr2 = curr2.next

        curr = new_list

        while(curr1 is not None and curr2 is not None):
            if(curr1.val <= curr2.val):
                curr.next = ListNode(curr1.val)
                curr1 = curr1.next
                curr = curr.next
            else:
                curr.next = ListNode(curr2.val)
                curr2 = curr2.next
                curr = curr.next
        
        if(curr1 is None and curr2 is not None):
            curr.next = curr2
        else:
            curr.next = curr1
        
        return new_list

