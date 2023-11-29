from typing import List


class Solution:
    def rotate(matrix:List[List[int]])->None:
        #do not return anything , rotation MUST BE DONE in-place
        l = 0 
        r = len(matrix)-1

        while l<r:
            for i in range(r-l):
                top  = l
                bottom = r

                #save the topleft
                topLeft = matrix[top][l+i]

                #move bottom left into top left
                matrix[top][l+i] = matrix[bottom-i][l]

                #move bottom right into bottom left
                matrix[bottom-i][l] = matrix[bottom][r-i]

                #move top right into bottom right
                matrix[bottom][r-i] = matrix[top+i][r]

                #move top left into top right
                matrix[top+i][r] = topLeft

            r -=  1
            l += 1

        print(matrix)

    rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])

    