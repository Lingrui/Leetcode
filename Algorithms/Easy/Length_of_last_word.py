#!/usr/bin/python

class Solution(object):
	def lengthOfLastWord(self,s):
		'''
		:type s: str
		:rtype: int
		'''
		words = s.split()
		if len(words) != 0:
			return len(words[-1])
		else: 
			return 0

if __name__ == '__main__':
	x = str(input("input a sentence: "))
	print(Solution().lengthOfLastWord(x))
