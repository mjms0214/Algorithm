# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if (l1.val+l2.val) // 10 == 0:
            output = ListNode(l1.val+l2.val, None)
            tmp = ListNode()
        else:
            output = ListNode((l1.val+l2.val)%10, None)
            tmp = ListNode((l1.val+l2.val) // 10, None)

        tail = output

        if l1.next == None and l2.next == None:
            if tmp.val != 0:
                output.next = tmp

        # 더 긴 리스트의 길이만큼 반복
        while l1.next != None or l2.next != None:

            # 앞부터 더하기
            if l1.next == None:
                l2 = l2.next
                sum_l1_l2 = l2.val + tmp.val
            elif l2.next == None:
                l1 = l1.next
                sum_l1_l2 = l1.val + tmp.val
            else:
                l1 = l1.next
                l2 = l2.next
                sum_l1_l2 = l1.val + l2.val + tmp.val
            # 10을 넘어가면 다음 노드에 1을 더하기
            # 10을 넘어간다면
            if sum_l1_l2 // 10 != 0:
                tmp.val = sum_l1_l2 % 10
                tail.next = tmp
                tmp.next = ListNode(sum_l1_l2 // 10, None)
            else:
                tmp.val = sum_l1_l2
                tail.next = tmp
                if l1.next == None and l2.next == None:
                    return output
                tmp.next = ListNode()
            
            tmp = tmp.next
            tail = tail.next

        return output
