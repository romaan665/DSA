class Solution(object):
    def maxProfit(self, prices):
        i=0
        cheapest=prices[0]
        maxx=0

        for i in prices:
            if i<cheapest:
                cheapest=i

            if i-cheapest>maxx:
                maxx=i-cheapest

        return maxx