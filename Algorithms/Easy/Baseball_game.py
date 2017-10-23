#!/usr/bin/python 

class Solution(object):
	def calPoints(self,ops):
		'''
		:type ops: List[str]
		:rtype: int 
		'''
		record = []
		for op in ops:
			if op == 'C':
				record.pop()
			elif op == 'D':
				record.append(record[-1]*2)
			elif op == '+':
				record.append(record[-1] + record[-2])
			else:
				record.append(int(op))
		return sum(record)


if __name__ == '__main__':
	x = (i for i in input("input score record:").split())
	print("Final score is:", Solution().calPoints(x))
