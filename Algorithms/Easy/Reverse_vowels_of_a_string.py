#!/usr/bin/python 
import re
class Solution(object):
	def reverseVowels(self,s):
		'''
		:type s: str
		:rtype: str
		'''
		vowels = re.findall('(?i)[aeiou]',s)
		#print (vowels)
		return re.sub('(?i)[aeiou]',lambda m:vowels.pop(),s)
		#return re.sub('(?i)[aeiou]','iiii',s)

if __name__ =='__main__':
	x = str(input("input a string:"))
	print(Solution().reverseVowels(x))
