# -*- coding: utf-8 -*-
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
"""

s = "azcbobobegghakl"

bobCount = 0

for i in range(len(s)):
    if s[i:].startswith("bob"):
        bobCount += 1
print("Number of times bob occurs is: " + str(bobCount))
