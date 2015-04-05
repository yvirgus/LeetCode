# Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Author : Yudistira Virgus
# Date   : 2015-04-04
#
# *****************************************************************************************************************************
# Problem 3
# Title : Longest Substring Without Repeating Characters 
# Difficulty : Medium
# Problem statement :
#
# Given a string, find the length of the longest substring without repeating characters. 
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
# For "bbbbb" the longest substring is "b", with the length of 1.
#
# *****************************************************************************************************************************
#
# Solution :
#
# The idea is using hash table to find the index of the last repeated character  
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        dic = {}
        ans, start = 0,-1
        
        for i,achar in enumerate(s):
            if achar in dic:
                start = max(start, dic[achar])
            dic[achar] = i
            ans = max(ans, i - start)
            
        return ans
