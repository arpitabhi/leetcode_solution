class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0])
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        print('transpose : {}'.format(matrix))
        for i in matrix:
            i.reverse()
        
        return matrix
            
        