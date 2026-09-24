class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict() # from sorted string to list of words
        for word in strs:
            sortedWord = ''.join(sorted(word))

            if sortedWord not in anagrams:
                anagrams[sortedWord] = [word]
            else:
                anagrams[sortedWord].append(word)

        words = []
        for sortedWord in anagrams:
            words.append(anagrams[sortedWord])

        return words