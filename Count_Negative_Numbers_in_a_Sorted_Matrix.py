class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for element_list_in_list in grid:
            
            l=0
            r=len(element_list_in_list)-1
            
            while r>=l:
                print('l and r :',l,r)
                median = l + (r-l)//2
                print('median : ',median)
                if (r-l)==1 or (r-l)==0:
                    if element_list_in_list[l] >=0 and element_list_in_list[r]>=0:
                        count+=len(element_list_in_list)-r-1
                        print('count : ',count)
                        break
                    elif element_list_in_list[l] <0 and element_list_in_list[r]<0:
                        count+=len(element_list_in_list)-l
                        print('count : ',count)
                        break
                    else:
                        count+=len(element_list_in_list)-r
                        print('count : ',count)
                        break
                    
                if element_list_in_list[median]>=0:
                    l=median+1
                elif element_list_in_list[median]<0:
                    r=median-1
        return count