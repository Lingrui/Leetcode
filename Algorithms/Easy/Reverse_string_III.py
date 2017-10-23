#!/usr/bin/python 

class Solution(object):
	def reverseWords(self,s):
		'''
		:type s : str
		:rtype: str 
		'''
		#return ' '.join(s.split()[::-1])[::-1]
		return ' '.join(word[::-1] for word in s.split())

if __name__ == '__main__':
	x = str(input("input a string:"))
	print(Solution().reverseWords(x))
