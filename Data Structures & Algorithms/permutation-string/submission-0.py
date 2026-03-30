class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        n,m=len(s1),len(s2)
        #gets the dictionary from s1 Eg {a:1,b3,c:2}
        count1 = Counter(s1) 
        #gets the dictionary from s2 Eg {a:4,b:4,c:5}
        window = Counter(s2[:n])
        #if both dictionary are equla that means the keys are equal it good to go
        if window == count1:
            return True
        
        for r in range(n,m):
            window[s2[r]]+=1
            window[s2[r-n]]-=1 # note we might be having some stuff that did not match on tope window==count() so - to make it the size of s1
            if window[s2[r-n]]==0:
                del window[s2[r-n]]
            if window == count1:
                return True
        return False
        