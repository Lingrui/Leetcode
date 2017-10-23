#!/usr/bin/python 

class Solution(object):
	def canWinNim(self,n):
		'''
		:type n : int 
		:rtype: bool
		'''
		return ( n%4 != 0 )
if __name__ == '__main__':
	x = int(input("input x :"))
	print("Stone number is:",Solution().canWinNim(x))
