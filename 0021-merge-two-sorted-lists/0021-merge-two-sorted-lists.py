# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        if list1 == None and list2 == None:
            return None

        while list1 != None or list2 != None:
            if list1 == None:
                l.append(list2.val)
                list2 = list2.next
            elif list2 == None:
                l.append(list1.val)
                list1 = list1.next
            elif list1.val > list2.val:
                l.append(list2.val)
                list2 = list2.next 
            elif list1.val < list2.val:
                l.append(list1.val)
                list1 = list1.next
            else:
                l.append(list1.val)
                l.append(list2.val)
                list1 = list1.next
                list2 = list2.next

        
        output = ListNode()
        for i, x in enumerate(l):
            if i == 0:
                output.val = x
            else:
                node = output
                while node.next != None:
                    node = node.next
                node.next = ListNode(x)

        return output

            
        