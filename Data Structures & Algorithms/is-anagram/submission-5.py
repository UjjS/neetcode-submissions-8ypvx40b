from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts1 = Counter(s)
        char_counts2= Counter(t)
        return char_counts1==char_counts2 