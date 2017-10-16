#!/usr/bin/python

class Solution(object):
	def detectCapitalUse(self,word):
		'''
		:type word: str
		:rtype: bool
		'''
		return word.isupper() or word.islower() or word.istitle()

if __name__ == '__main__':
	x = str(input("input a string:"))
	print("Capital detection:",Solution().detectCapitalUse(x))

