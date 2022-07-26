# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        na=headA
        nb=headB
        d={}
        while na is not None:
            d[na]=na.val
            na=na.next
            
        while nb is not None:
            if nb in d:
                return nb
            nb=nb.next
        
        return None
        
        