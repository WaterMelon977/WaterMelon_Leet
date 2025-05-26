class Solution:
    def trap(self, height: List[int]) -> int:
        # o(n)but beats only 23% and O(n) space 
        maxL=[0]
        maxR=[0]
        length=len(height)
        maxl=0
        maxr=0
        for idx in range(1,length):
            maxl=max(maxl,height[idx-1])
            maxL.append(maxl)
            maxr=max(maxr,height[length-idx])
            maxR.append(maxr)
        maxR.reverse()
        
        water=0
        for i in range(1,length-1):
            potential= min(maxL[i],maxR[i])
            if potential>height[i]:
                water+=potential-height[i]
        return water 
    

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        l,r=0,len(height)-1
        lmax,rmax=height[l],height[r]
        ans=0
        while l<r:
            if lmax<rmax:
                l+=1
                lmax=max(lmax,height[l])
                ans+=lmax-height[l]
            else:
                r-=1
                rmax=max(rmax,height[r])
                ans+=rmax-height[r]
        return ans