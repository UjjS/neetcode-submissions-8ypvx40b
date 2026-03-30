class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i > 0 and nums[i-1]==nums[i]:
                continue
            
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j-1]==nums[j]:
                    continue
                l=j+1
                r=len(nums)-1
                while l<r:
                    total= nums[i]+nums[j]+nums[l]+nums[r]
                    if total<target:
                        l+=1
                    elif total>target:
                        r-=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])

                        while l<r and nums[l+1]==nums[l]:
                            l+=1
                        while l<r and nums[r-1]==nums[r]:
                            r-=1
                        l+=1
                        r-=1
        return res

        