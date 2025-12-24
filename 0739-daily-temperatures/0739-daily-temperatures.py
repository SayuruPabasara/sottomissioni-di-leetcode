class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack=[]
        n=len(temperatures)
        answer=[0]*n
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                index=stack.pop()
                answer[index]=i-answer[index]
            stack.append(i)
        return answer    
        