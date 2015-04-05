# Source : https://leetcode.com/problems/merge-k-sorted-lists/
# Author : Yudistira Virgus
# Date   : 2015-04-05
#
# *****************************************************************************************************************************
# Problem 23
# Title : Merge k Sorted Lists 
# Difficulty : Hard
# Problem statement :
# 
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# *****************************************************************************************************************************
#
# Solution :

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if not lists: return None 
        if len(lists) == 1: return lists[0]
        
        sorted_listNodes = []
        
        for head in lists:
            while head:
                sorted_listNodes.append(head)
                head = head.next
                
        sorted_listNodes.sort(key=self.f)
        
        for i in range(len(sorted_listNodes) -1):
            sorted_listNodes[i].next = sorted_listNodes[i+1]
        
        return sorted_listNodes[0] if sorted_listNodes else None
        
    def f(self, aListNode):
        return aListNode.val

# Complexity : currently it is O(n*lg(n)), where n is the total number of nodes, because we sort all the nodes.
# This can be improved to O(n*lg(k)) with mergeTwoLists function as shown below.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        lt = len(lists)
        if lt == 0: return None
        if lt == 1: return lists[0]
        if lt == 2: return self.mergeTwoLists(lists[0], lists[1])
        return self.mergeTwoLists( self.mergeKLists( lists[:(lt//2)] ), self.mergeKLists( lists[(lt//2):] ))

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        head = tmp = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next

            tmp = tmp.next

        if l1 or l2:
            tmp.next = l1 or l2

        return head.next

# But the second solution is much slower in LeetCode OJ. Why?
