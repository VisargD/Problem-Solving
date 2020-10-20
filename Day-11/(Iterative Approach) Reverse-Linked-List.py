"""
Problem Name: Reverse Linked List
Platform: Leetcode
Difficulty: Easy
Problem Link: https://leetcode.com/problems/reverse-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # On every iteration, change the 'next' pointer of node to the previous node and then move all the pointers by 1.
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev


# For example, INPUT: 1->2->3->4->5->NULL
# Then iterations will look like:
#       Initially prev=NULL, head = first node.
#       NULL<-1 2->3->4->5->NULL (AFTER: prev= first node, head = second node)
#       NULL<-1<-2 3->4->5->NULL (AFTER: prev= second node, head = third node)
#       NULL<-1<-2<-3 4->5->NULL (AFTER: prev= third node, head = fourth node)
#       NULL<-1<-2<-3<-4 5->NULL (AFTER: prev= fourth node, head = fifth node)
#       NULL<-1-<2<-3<-4<-5 NULL (AFTER: prev= fifth node, head = NULL)

# All the next pointers will be reversed now. So returning prev will give us the following reversed list:
#       5->4->3->2->1->NULL
