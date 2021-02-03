import copy
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        #Solution 1 Issues with identity element indexing in output
        
        t=copy.deepcopy(nums)
        nums.sort()
        print('sorted : {}'.format(nums))
        l=0
        r=len(nums)-1
        while r>l:
            if nums[l]+nums[r]==target:
                print('l : {}, r : {}'.format(nums[l],nums[r]))
                return [t.index(nums[l]),t.index(nums[r])]
            elif nums[l]+nums[r]>target:
                r=r-1
            else:
                l=l+1
        return -1
        
        '''
        
        #Solution 2
        for i in range(len(nums)-1):
            remain=target-nums[i]
            if remain in nums[i+1:]:
                return [i,nums[i+1:].index(remain)+i+1]
        
        
        
            
        
        
        