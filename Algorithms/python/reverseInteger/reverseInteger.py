# Source : https://leetcode.com/problems/reverse-integer/
# Author : Yudistira Virgus
# Date   : 2015-04-04
#
# *****************************************************************************************************************************
# Title : Reverse Integer
# Problem statement :
#
# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# *****************************************************************************************************************************
#
# Solution :
#
# With type casting to str :
class Solution:
    # @return an integer
    def reverse(self, x):
        if x == 0: return 0 
        result = int(str(abs(x))[::-1])*x/abs(x)
        return result if abs(result) < 2**31 else 0

# Without type casting to str :
class Solution:
    # @return an integer
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x *= sign
        ans, n = 0, 10
        digits = []

        while x:
            digit = (x%n)//(n/10)
            digits.append(digit)
            x -= x%n
            n *= 10
            
        for digit in digits:
            ans += digit*n/100
            n /= 10
            
        return ans*sign if ans < 2**31 else 0
