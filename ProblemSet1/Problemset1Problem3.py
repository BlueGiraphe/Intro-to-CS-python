# -*- coding: utf-8 -*-
"""
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order.
"""

s = 'azcbobobegghakl'

maxLen = 0
current = s[0]
longest = s[0]

for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        current += s[i + 1]
        if len(current) > maxLen:
            maxLen = len(current)
            longest = current
    else:
        current = s[i + 1]

print ('Longest substring in alphabetical order is: ' + longest)
    