#!/usr/bin/python 

class Solution(object):
	def distributeCandies(self,candies):
		'''
		:type candies: List[int]
		:rtype: int
		'''
		return int(min(len(candies)/2,len(set(candies))))
		 
if __name__ == '__main__':
	x = [int(i) for i in input("input candies:" ).split()]
	print("Max candy kinds:",Solution().distributeCandies(x))

