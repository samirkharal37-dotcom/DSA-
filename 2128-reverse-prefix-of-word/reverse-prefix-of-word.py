class Solution(object):
    def reversePrefix(self, word, ch):
        n=word.find(ch)

        if n==-1:
            return word
        else:
            temp=word[:n+1]
            result=temp[::-1]+word[n+1:]
        return result