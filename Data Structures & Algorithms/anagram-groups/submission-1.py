from collections import defaultdict
class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in words:
            key = tuple(sorted(word))
            mp[key].append(word)
        return list(mp.values())