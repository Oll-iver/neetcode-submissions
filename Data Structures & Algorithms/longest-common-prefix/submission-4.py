class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first=strs[0]
        letters=[]
        for letter in first:
            letters.append(letter)
        counts=[]
        for word in strs:
            count=0
            i=0
            while i<len(word) and i<len(letters) and letters[i] == word[i]:
                count+=1
                i+=1
            counts.append(count)

        return first[:min(counts)]