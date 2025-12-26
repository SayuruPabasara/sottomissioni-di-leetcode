class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        time=0
        while tickets[k]>=0:
            if tickets[0]>0:
                tickets[0]-=1
                time+=1
                if tickets[0]==0:
                    tickets.pop(0)
                else:
                    tickets.append(tickets.pop(0))
        return time
        
