#!/usr/bin/python 
'''
the key to this problem is to figure out the connection between the output and the input, which is quite clear that the link between them is that their sum equals to nearest 2^n-1 greater than num. 
'''
class Solution(object):
	def findComplement(self,num):
		"""
		:type num: int 
		:rtype: int 
		"""
		i = 1 
		while i <= num:
		 	i = i << 1
		return (i - 1) ^ num

if __name__ == '__main__':
	x = int(input("input x :"))
	print("Complement number is:",Solution().findComplement(x))

