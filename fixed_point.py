class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        '''
        l=0
        r=len(arr)-1
        fixed_point_arr=[]
        while r>l:
            mid=l+((r-l)//2)
            if (r-l)==2 or (r-l)==1:
                if arr[l]==l:
                    fixed_point_arr.append(l)
                    break
                elif arr[mid]==mid:
                    fixed_point_arr.append(mid)
                    break
                elif arr[r]==r:
                    fixed_point_arr.append(r)
                    break
                else:
                    break
            if arr[mid]==mid:
                print('mid : {}, l : {}, r : {}'.format(mid,l,r))
                fixed_point_arr.append(mid)
                r=mid-1
            elif arr[mid]>mid:
                print('mid : {}, l : {}, r : {}'.format(mid,l,r))
                r=mid-1
            else:
                print('mid : {}, l : {}, r : {}'.format(mid,l,r))
                l=mid
        if len(fixed_point_arr)>0:
            return min(fixed_point_arr)
        else:
            return -1
        '''
        
        
        
        for i,element in enumerate(arr):
            if element==i:
                return i
            
        return -1