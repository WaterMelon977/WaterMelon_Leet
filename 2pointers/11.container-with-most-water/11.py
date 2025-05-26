class Solution:
    def maxArea(self, height: List[int]) -> int:
        L=0
        R=len(height)-1
        max_water=0


        while L<R :
            hl=height[L]
            hr=height[R]
            water=(R-L)*min(hl,hr)
            if water>max_water :
                max_water=water
            if hl> hr:
                R-=1
            else:
                L+=1
           

        return max_water
    

            