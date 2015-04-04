# Source : https://leetcode.com/problems/add-two-numbers/
# Author : Yudistira Virgus
# Date   : 2015-04-04
#
# *****************************************************************************************************************************
# Title : Add Two Numbers
# Problem statement :
#
# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
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
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = tmp = ListNode(0)
        
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            tmp.next = ListNode((l1_val + l2_val + carry)%10)
            carry = (l1_val + l2_val + carry)//10
            
            tmp = tmp.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        if carry:
            tmp.next = ListNode(carry)
        
        return head.next
