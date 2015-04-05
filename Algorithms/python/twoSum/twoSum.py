# Source : https://leetcode.com/problems/two-sum/
# Author : Yudistira Virgus
# Date   : 2015-04-04
#
# *****************************************************************************************************************************
# Problem 1 
# Title : Two Sum
# Problem statement :
#
# Given an array of integers, find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, 
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
#
# *****************************************************************************************************************************
#
# Solution :

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        # This assumes that there is exactly one solution
        if target %2 == 0 and num.count(target/2) > 1:
            i = num.index(target/2)
            j = num[i+1:].index(target/2) + i + 1
            return i+1, j+1
        
        table = dict(zip(num, range(len(num))))
        
        for i in range(len(num)-1):
            if ((target - num[i]) in table) and (target != 2*num[i]):
                return i+1, table[target - num[i]] + 1
