class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower():
            return True
        if word[0].isupper() and word[1:len(word)].islower():
            return True
        else:
            return False

        