class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        unique = dict()
        for word in strs:
            sort = "".join(sorted(word))
            if sort in unique:
                unique[sort].append(word)
            else:
                unique[sort] = [word]
        
        for entry in unique:
            res.append(unique[entry])

        return res