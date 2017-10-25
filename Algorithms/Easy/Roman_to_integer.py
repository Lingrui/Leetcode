#!/usr/bin/python 

class Solution(object):
	def romanToInt(self,s):
		'''
		:type s:str
		:rtype: int 
		'''
		number = 0 
		roman = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
		for i in range(0,len(s)-1):
			if roman[s[i]] < roman[s[i+1]]:
				number -= roman[s[i]]
			else:
				number += roman[s[i]]
		number += roman[s[-1]]
		return number 

if __name__ == '__main__':
	x = str(input("input a roman number: "))
	print (Solution().romanToInt(x))
