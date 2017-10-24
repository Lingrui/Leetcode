#!/usr/bin/python 

from collections import Counter
class Solution(object):
	def canConstruct(self,ransomNote,magazine):
		'''
		:type ransomNote: str
		:type magaZine: str
		:rtype: bool 
		'''
		print (Counter(ransomNote))
		return not Counter(ransomNote) - Counter(magazine)

if __name__ == '__main__':
	x = str(input("input ransomNote: "))
	y = str(input("input magazine: "))
	print(Solution().canConstruct(x,y))
