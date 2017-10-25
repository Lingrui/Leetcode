#!/usr/ibn/python 

class Solution(object):
	def validPalidrome(self,s):
		'''
		:type s: str
		:rtype: bool
		'''
		i = 0 
		length = len(s)/2
		while i < length and s[0] == s[-1]:
		#while i <= (len(s)+1)/2 and s[i] == s[-(i+1)]:
			i += 1
			print ("i:",i)
			print ("length:",len(s))
			s = s[1:-1]
			#s = s[i:len(s) - i]
			print ("string:",s)
			print ()
		return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1] 

if __name__ == '__main__':
	x = str(input("input a string: "))
	print(Solution().validPalidrome(x))
