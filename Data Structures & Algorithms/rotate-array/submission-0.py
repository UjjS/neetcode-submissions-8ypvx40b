class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums)<1:
            return
        k=k%len(nums)
        nums[::]= nums[-k:]+nums[:-k]
        return nums

        