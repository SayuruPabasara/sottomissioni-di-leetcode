class Solution(object):
    def finalPrices(self, prices):
        answer=list(prices)
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if j>i and prices[j]<=prices[i]:
                    answer[i]-=prices[j]
                    break
        return answer     

        