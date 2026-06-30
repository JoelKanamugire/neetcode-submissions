class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        new_word = []
        while i < len(word1) and j < len(word2):
            new_word.append(word1[i])
            new_word.append(word2[j])
            i = i + 1
            j = j + 1

        new_word.append(word1[i:])
        new_word.append(word2[j:])

        return "".join(new_word)
        
        