class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        '''
        #Solution 1
        #Brute force
        
        
        distinct=[]
        for i in nums:
            if i not in distinct:
                distinct.append(i)
        dict1=[]
        for i in distinct:
            count=0
            for j in nums:
                if i==j:
                    count+=1
            dict1.append((count,i))
        dict1.sort()
        if dict1[-1][1] == target and dict1[-1][0] > (len(nums)/2):
            return True
        else:
            return False
        '''
        
        #Solution 2
        # Somewhat optimized
        
        count=0
        for i in nums:
            if i==target:
                count+=1
        if count>(len(nums)/2):
            return True
        else:
            return False
            
        
        '''
        #Solution 3
        
        #left most index of target element
        l=0
        r=len(nums)-1
        left=None
        if r>0:
            while r>l:
                mid=l+((r-l)//2)
                print('mid : {},l : {}, r : {}'.format(mid,l,r))
                if (r-l)==1:
                    if nums[l]==target:
                        left=l
                        print('first')
                    elif nums[r]==target:
                        left=r 
                        print('Second')
                    break
                if nums[mid]==target:
                    r=mid
                elif nums[mid]<target:
                    l=mid
                else:
                    r=mid
            print(left)
            if left is not None:
                print(left)
            else:
                print('Error in finding left')

            #right most index of target element
            l=0
            r=len(nums)-1
            right=None
            while r>l:
                mid=l+((r-l)//2)
                print('mid : {},l : {}, r : {}'.format(mid,l,r))
                if (r-l)==1:
                    if nums[r]==target:
                        right=r
                    elif nums[l]==target:
                        right=l                   
                    break
                if nums[mid]==target:
                    l=mid
                elif nums[mid]>target:
                    r=mid
                else:
                    l=mid
            if right:
                print(right)
            else:
                print('Error in finding right')

            if right is not None and left is not None:
                final = right-left+1
                if final>(len(nums)/2):
                    return True
                else:
                    return False
            else:
                return False
        else:
            if target in nums:
                return True
            else:
                return False
        
        '''