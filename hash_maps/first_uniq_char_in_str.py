# DSA of the Day - Day 3
# Concept: Hash Maps
#
# Problem: First Unique Character in a String
#
# Given a string s, find the first non-repeating character in it
# and return its index. If it does not exist, return -1.
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Explanation: 'l' is the first character that does not repeat.
#
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Explanation: 'v' is the first character that does not repeat.
#
# Example 3:
# Input: s = "aabb"
# Output: -1
# Explanation: No non-repeating character exists.
#
# Hints:
# 1. Use a hash map (dictionary in Python) to count character frequencies.
# 2. Then scan through the string to find the first char with count = 1.

def first_unique_char(givenString):
	seen = {}
	for letter in givenString:
		if letter in seen:
			seen[letter] = False
		else:
			seen[letter] = True

	for i, letter in enumerate(givenString):
		if seen[letter] == True:
			return i
	return -1

