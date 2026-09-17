class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen={}
        seent={}
        for letter in s:
            if letter in seen:
                seen[letter]+=1 
            else:
                seen[letter]=1
        for letter in t:
            if letter in seent:
                seent[letter]+=1
            else:
                seent[letter]=1
        if seen==seent:
            return True
        return False