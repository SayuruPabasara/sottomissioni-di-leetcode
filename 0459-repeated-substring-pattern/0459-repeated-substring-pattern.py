class Solution(object):
    def repeatedSubstringPattern(self, s):
        counts=[]
        
        if s:
            for i in s:
                count=s.count(i)
                counts.append(count)
                k=len(counts)
            counts_set=set(counts)
            if len(counts_set)==1 and k>1:
                return True
        return False        
        
        