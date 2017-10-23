#!/usr/bin/python 

class Solution(object):
	def fizzBuzz(self,n):
		'''
		:type n: int
		:rtype: List[str]
		'''
		fb = []
		for i in range(1,n+1):
			if i%15 == 0 :
				fb.append("FizzBuzz")
			elif i%3 == 0:
				fb.append("Fizz")
			elif i%5 == 0:
				fb.append("Buzz")
			else:
				fb.append(str(i))

		return fb
if __name__ == '__main__':
	x = int(input("input x: "))
	print (Solution().fizzBuzz(x))

				
