#!/usr/bin/python 

class Solution(object):
	def hammingDistance(self,x,y):
		"""
		:type x: int 
		:type y: int
		:rtype: int 
		"""
		return bin(x^y).count('1')

if __name__ == '__main__':
	x = int(input("input x :"))
	y = int(input("input y :"))
	print("Hamming Distance:",Solution().hammingDistance(x,y))
