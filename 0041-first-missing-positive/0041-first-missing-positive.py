class Solution(object):
    def firstMissingPositive(self, nums):
        nums=list(sorted(set(nums)))
        i=1
        for n in nums:
            if n>0:
                if n!=i:
                    return i
                else:
                    i+=1
        return i
        


        