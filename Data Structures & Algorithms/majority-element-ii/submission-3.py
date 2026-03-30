class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n= len(nums)
        num1=num2=-1
        ct1=ct2=0

        for num in nums:
            if num == num1:
                ct1+=1
            elif num == num2:
                ct2+=1
            elif ct1 ==0:
                ct1=1
                num1=num
            elif ct2 ==0:
                ct2=1
                num2=num
            else:
                ct2-=1
                ct1-=1
            
        cnt1=cnt2=0

        for num in nums:
            if num == num1:
                    cnt1+=1
            elif num == num2:
                    cnt2+=1
        
        res = []
        if cnt1 > n // 3:
                res.append(num1)
        if cnt2 > n // 3:
                res.append(num2)
        
        return res

