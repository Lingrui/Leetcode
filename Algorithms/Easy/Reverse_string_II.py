#!/usr/bin/python 

class Solution(object):
	def reverseStr(self,s,k):
		'''
		:type s: str
		:type k: int
		:rtype: str
		'''
		s = list(s)
#k = int(k)
		for i in range(0,len(s),2*k):
			s[i:i+k] = reversed(s[i:i+k])
		return "".join(s)

if __name__ == '__main__':
	x = str(input("input a string:"))
	y = int(input("input step:"))
	print(Solution().reverseStr(x,y))
