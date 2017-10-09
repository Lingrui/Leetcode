#!/usr/bin/python
from collections import Counter

class Solution:
	def judgeCircle(self,moves):
		'''
		:type moves: str
		:rtype: bool
		'''
		c = Counter(moves)
		return c['L'] == c['R'] and c['U'] == c['D']

if __name__ == '__main__':
	x = str(input("input moves:"))
	print("Is it a circle? :",Solution().judgeCircle(x))

