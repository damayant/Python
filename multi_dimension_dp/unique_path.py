class Solution:
    def uniquePaths(m:int,n:int)->int:
        row = [1] * n

        for i in range(m-1):
            new_row = [1] * n
            for j in range(n-2, -1 , -1):
                new_row[j] = new_row[j+1] + row[j]
            row =  new_row
        print(row[0])
        return row[0]

    uniquePaths(m = 3, n = 7)      