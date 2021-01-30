class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        while r>l:
            print('r and l',r,l)
            median = l + ((r-l)//2)
            print('median : ',median)
            if arr[median-1]<arr[median] and arr[median]>arr[median+1]:
                print('final : ',median)
                return median
            elif arr[median-1]<arr[median] and arr[median]<arr[median+1]:
                l=median
            else:
                r=median
        