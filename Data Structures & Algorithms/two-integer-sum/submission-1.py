# from typing import DefaultDict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            curr_no=target-nums[i]
            print(curr_no)
            print(mp)
            if (curr_no in mp):
                return [mp[curr_no],i]
            mp[nums[i]]=i
        return []

