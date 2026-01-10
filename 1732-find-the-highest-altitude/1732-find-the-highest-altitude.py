class Solution(object):
    def largestAltitude(self, gain):
        highest=0
        sums=0
        for g in gain:
            sums+=g
            highest=max(sums,highest)
        return highest


        