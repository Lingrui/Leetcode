#!/usr/bin/python 

class Solution(object):
	def maxProfit(self,prices):
		'''
		:type prices: List[int]
		:rtype: int 
		'''
		pro = 0
		if (len(prices) >= 1):
			price_min = prices[0]
		for i in range(1,len(prices)):
			if ((prices[i]-price_min) > pro):
				pro = prices[i] - price_min
			if (prices[i] < price_min):
				price_min = prices[i]
		
		return pro


if __name__ == '__main__':
#x = list(int,input("input a price list :"))
	x = [int(i) for i in input("input a price list :").split()]
	print("Maximum profit is :",Solution().maxProfit(x))
					
