class Solution:
    
    def binary_search(self,arr,l,r,x):
        while r>=l:
            mid=l+((r-l)//2)
            print('mid : {}, l : {}, r : {}'.format(mid,l,r))
            if arr[mid]==x:
                return mid
            elif arr[mid]>x:
                r=mid-1
            else:
                l=mid+1
        return -1
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        for i in range(len(numbers)):
            remaining_num=target-numbers[i]
            print('remaining_num : ',remaining_num)
            if remaining_num>=0:
                j=i+1
                k=len(numbers)-1
                print('numbers : {}, j : {}, k : {}, remaining_num : {}'.format(numbers,j,k,remaining_num))
                other=self.binary_search(numbers,j,k,remaining_num)
                print('other : ',other)
                if other>0:
                    return [i+1,other+1]
            else:
                break
    '''
        l=0
        r=len(numbers)-1
        while r>l:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r]>target:
                r-=1
            else:
                l+=1