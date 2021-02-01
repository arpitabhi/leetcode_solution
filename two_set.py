class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elements=[]
        '''
        for i in nums1:
            if i in nums2 and i not in elements:
                elements.append(i)
                    
        return elements
        '''
        set1=set(nums1)
        set2=set(nums2)
        for i in set1.intersection(set2):
            if i not in elements:
                elements.append(i)
                
        return elements
                    