#!/usr/bin/python 

class Solution(object):
	def isPalidrome(self,s):
		'''
		:type s: str
		:rtype: bool
		'''
#array = [i for i in s.lower() if i.isalnum()]
		array = [i.lower() for i in s  if i.isalnum()]
		print (array)
		return array == array[::-1]

if __name__ == '__main__':
	x = str(input("input a string:"))
	print(Solution().isPalidrome(x))
