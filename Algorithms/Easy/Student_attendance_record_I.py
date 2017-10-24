#!/usr/bin/python 

class Solution(object):
	def checkRecord(self,s):
		'''
		:type s: str
		:rtype: bool
		'''

		return s.count('A')<2 and s.count('LLL')==0 #count faster than find
		#return s.count('A')<2 and s.find('LLL')==-1

if __name__ == '__main__':
	x = input("input a string: ")
	print (Solution().checkRecord(x))
