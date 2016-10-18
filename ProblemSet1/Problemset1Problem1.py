# -*- coding: utf-8 -*-
"""
Write a program that counts the  number of vowels contained in the string s.
Valid vowels are 'a', 'e', 'i', 'o' and 'u'.
"""

s = 'azcbobobegghakl'
vowelCount = 0
vowel = "aieouAIEOU"

for letter in s:
    if letter in vowel:
        vowelCount +=1
print("Number of vowels: " + str(vowelCount))