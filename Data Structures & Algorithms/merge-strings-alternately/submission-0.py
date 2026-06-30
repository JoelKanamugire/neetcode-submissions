class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        newWord = []

        while i < len(word1) and j < len(word2):
            newWord.append(word1[i])
            newWord.append(word2[j])
            i+=1
            j+=1

        newWord.append(word1[i:])
        newWord.append(word2[j:])

        return "".join(newWord)



        