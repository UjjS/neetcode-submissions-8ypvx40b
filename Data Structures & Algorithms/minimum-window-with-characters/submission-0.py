class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT,window={},{}
        for i in range(len(t)):
            countT[t[i]]=1+ countT.get(t[i],0)
        have,need=0,len(countT)
        res,resLength=[-1,-1],float("inf")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]= 1+window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have+=1
                #ye count kr rha h ki c h ki nhi aur agar h to kiya c countT wala h
            while have==need:
                if (r-l+1)<resLength:
                    res=[l,r]
                    resLength=(r-l+1)
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLength != float("inf") else ""

