class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size= float("inf")
        l,total= 0, 0
        for r in range(len(nums)):
            total+=nums[r]
            while total>= target:
                total-=nums[l]
                size= min(r-l+1,size)# this one gets size
                l+=1
        return 0 if size==float('inf') else size
                
