class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        list1=[]
        string=''
        for i in s:
            if i in string:
                index=string.index(i)
                list1.append(string)
                string=string[index+1:]+i
            else:
                string+=i
                
        list1.append(string)
        max=0
        for j in list1:
            if len(j)>max:
                max=len(j)
                
        return max