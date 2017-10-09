#!/usr/bin/python 

class Solution(object):
	def arrayPairSum(self,nums):
		"""
		: type nums: List[int]
		: rtype: int
		"""
		sum_pair = 0
		tmp = sorted(nums,key=int)
		#print (tmp)
		for i in range(0,len(tmp)):
			#print (i)
			if (i%2 == 0):
				#print ("yes")
				#print (tmp[i])
				sum_pair += tmp[i]

		return sum_pair


if __name__ == '__main__':
	x = [int(i) for i in input("input a price list :").split()]
	print("Maximum sum of pairs is :",Solution().arrayPairSum(x))

