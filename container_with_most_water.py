class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        #Solution 1
        #Brute Force solution
        n=len(height)
        p=0
        for i in range(n-1):
            for j in range(i,n):
                if height[i]<=height[j]:
                    area=height[i]*(j-i)
                else:
                    area=height[j]*(j-i)
                if area>p:
                    p=area
        return p
        '''
        #Solution 2
        l=0
        r=len(height)-1
        max_area=0
        while r>l:
            if height[l]==height[r]:
                area=height[l]*(r-l)
                if height[l+1]<=height[r-1]:
                    r-=1
                else:
                    l+=1
            elif height[l]<height[r]:
                area=height[l]*(r-l)
                l+=1
            else:
                area=height[r]*(r-l)
                r-=1
            if area>max_area:
                max_area=area
        return max_area
        