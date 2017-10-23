#!/usr/bin/python 

class Solution(object):
	def findLUSlength(self,a,b):
		'''
		:type a : str
		:type b : str
		:rtype: int 
		'''
		if a == b:
			return -1
		else:
			return max(len(a),len(b))

if __name__ == '__main__':
	x = str(input("input string A:"))
	y = str(input("input string B:"))
	print("Longest uncommon subsequence length is: ",Solution().findLUSlength(x,y))
