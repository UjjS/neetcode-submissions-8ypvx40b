class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        # put numbers in right place
        while i < n:
            correct = nums[i] - 1   # where this number should go
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                # swap into correct place
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        # now check which index is wrong
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # if all are right → next number
        return n + 1