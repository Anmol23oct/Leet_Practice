# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        curr=head
        currh=head
        newHead=None
        prev=None
        count=k
        while curr is not None :
            curr=curr.next
            count-=1
            if count==0:
                count=k
                newH,tail=self.reverse(currh,curr,prev)
                if newHead is None:
                    newHead=newH
                prev=currh
#         print("prev=",prev.data)
                currh=prev.next
                curr=currh
        
        return newHead
#         curr=head
#         start=head
#         num=k
#         flag=True
#         prev=None
#         while curr is not None :
#             curr=curr.next
#             num-=1
#             if num==0:
#                 num=k
#                 print("b",start.val)
#                 print("prev",prev)
#                 start,prevf=self.reverse(start,curr,prev)
#                 print("a",start.val)
#                 if flag:
#                     head=start
#                     flag=False
#                 print("curr",curr)
#                 print("prevf",prevf)
                
#                 start=curr
#                 prev=prevf
        
#         return head
            
    def reverse(self,head,tail,prev):
        
        curr=head
        prevf=None
#     printLinkedList(head)
#     print("headbefore=,",head.data)
#     print("tailbefore=,",tail.data)
#     if prev is not None:
#         print("prev=,",prev.data)
        while curr is not None and not(curr==tail):
        
            next=curr.next
            if prevf is None:
                curr.next=tail
            else:
                curr.next=prevf
            prevf=curr
            curr=next
            if not(curr==tail):
                head=curr
        print(prevf)
        if prevf is not None and prev is not None:
        
            prev.next=prevf
    
#     printLinkedList(head)
#     print("head=,",head.data)
#     print("pervf=,",prevf.data)
        return head,prevf
        
#         head=start
#         prevf=start
#         while head is not curr:
            
#             #print(head.val)
#             nexts=head.next
#             head.next=prev
#             prev=head
#             head=nexts
        
#         #test=tail
#         # print("tail",tail)
#         # print("head",head)
#         prev.next=curr
#         print("prev in loop",prev)
#         # while test:
#         #     print("test",test.val)
#         #     test=test.next
        
#         return prev,prevf
            
            
            
        