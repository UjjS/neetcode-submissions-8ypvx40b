from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_dict = dict(sorted(count.items(),key=lambda x : x[1],reverse=True))
        sorted_list= list(sorted_dict.keys())
        return sorted_list[:k]
       