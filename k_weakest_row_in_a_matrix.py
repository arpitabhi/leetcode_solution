class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dict1={}
        key = 0
        for list_in_mat in mat:
            l=0
            r=len(list_in_mat)-1
            
            count=0
            while r>l:
                mid = l + ((r-l)//2)
                print('median, l, r are : ',mid,l,r)
                if list_in_mat[mid] == 1 and list_in_mat[mid+1] == 0:
                    count=mid+1
                    print('count : ',count)
                    dict1[key]=count
                    break
                elif list_in_mat[mid] == 1:
                    if (r-l)==1:
                        count=len(list_in_mat)
                        print('count : ',count)
                        dict1[key]=count
                        break
                    else:
                        l=mid
                        print('l : ',l)
                else:
                    if (r-l)==1:
                        count=0
                        print('count : ',count)
                        dict1[key]=count
                        break
                    else:
                        r=mid
                        print('r : ',r)
            key+=1
        print(dict1)
        result=sorted(dict1.items(), key = lambda kv:(kv[1], kv[0]))
        final=[]
        for i in range(k):
            final.append(result[i][0])
        return final
            