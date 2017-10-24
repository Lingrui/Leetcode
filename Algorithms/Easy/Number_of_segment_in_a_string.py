#!/usr/bin/python 

class Solution(object):
	def countSegments(self,s):
		'''
		:type s: str
		:rtype: int 
		'''
		return len(s.split())

if __name__ == '__main__'
	x = str(input("input a string:"))
	print(Solution().countSegments(x))
