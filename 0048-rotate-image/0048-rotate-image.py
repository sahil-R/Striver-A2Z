class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i <j:
                    temp=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=temp
        for i in range(len(matrix)):
            # left=0
            # right=len(matrix[0])-1
            # while left<=right:
            #     temp=matrix[i][left]
            #     matrix[i][left]=matrix[i][right]
            #     matrix[i][right]=temp
            #     left+=1
            #     right-=1
            matrix[i]=matrix[i][::-1]
        