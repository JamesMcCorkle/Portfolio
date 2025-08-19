class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)   #dummy node
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:   #compare values
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        #attach the remainder
        tail.next = list1 if list1 else list2

        return dummy.next
