#!/usr/bin/python 

class Solution(object):
	def reverseString(self,s):
		'''
		:type s : str
		:rtype: str 
		'''
		return s[::-1]

if __name__ == '__main__':
	x = str(input("input a string:"))
	print("Reversed string is :",Solution().reverseString(x))
