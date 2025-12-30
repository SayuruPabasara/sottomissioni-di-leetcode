class Solution(object):
    def rotateString(self, s, goal):
        if len(s)==len(goal):
            s=list(s)
            goal=list(goal)
            k=0
            while k<=len(s):
                if s==goal:
                    return True
                s.append(s.pop(0)) 
                k+=1
            return False
        else:
            return False
        