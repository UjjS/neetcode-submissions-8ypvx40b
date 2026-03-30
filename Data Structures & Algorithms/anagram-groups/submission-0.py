from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
    
        for word in strs:
        # Use sorted tuple as key
            key = tuple(sorted(word))
            anagram_map[key].append(word)
    
        return list(anagram_map.values())
        
            
            