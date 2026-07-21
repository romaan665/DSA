class Solution(object):
    def isAnagram(self, s, t):
        sfreq={}
        tfreq={}

        for i in s:
            if i not in sfreq:
                sfreq[i]=1
            else:
                sfreq[i]+=1
        for j in t:
            if j not in tfreq:
                tfreq[j]=1
            else:
                tfreq[j]+=1

        return sfreq==tfreq
        