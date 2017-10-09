#!/usr/bin/python

class Solution:
	def judgeCircle(self,moves):
		'''
		:type moves: str
		:rtype: bool
		'''
		return len(moves)%2 == 0 and moves.count('U')==moves.count('D') and moves.count('L')==moves.count('R')

if __name__ == '__main__':
	x = str(input("input moves:"))
	print("Is it a circle? :",Solution().judgeCircle(x))

