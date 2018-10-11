class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 and l2 ) :
            if l1.val >= l2.val :
                res = l2 
                l2 = l2.next
            else :
                res = l1
                l1 = l1.next 
            temp = res 
            while (l1 and l2) :
                if l1.val >= l2.val :
                    temp.next = l2
                    l2 = l2.next
                    temp = temp.next
                else :
                    temp.next = l1 
                    l1 = l1.next
                    temp = temp.next
            if (l1):
                temp.next = l1
            else :
                temp.next = l2
        elif l1 :
            res = l1
        else  :
            res = l2
        return res 