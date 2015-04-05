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
# This can be improved to O(n*lg(k)) with mergeTwoLists function.
