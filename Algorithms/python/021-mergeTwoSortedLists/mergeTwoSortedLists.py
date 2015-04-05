# Source : https://leetcode.com/problems/merge-two-sorted-lists/
# Author : Yudistira Virgus
# Date   : 2015-04-05
#
# *****************************************************************************************************************************
# Problem 21 
# Title : Merge Two Sorted Lists
# Difficulty : Easy
# Problem statement :
#
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.
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
    # @param two ListNodes
    # @return a ListNode
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
