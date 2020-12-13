'''
You are provided with the number of rows (R) and columns (C). Your task is to generate the matrix having R rows and C columns such that all the numbers are in increasing order starting from 1 in row wise manner.

Input Format:
The first line contain two numbers R and C separated by a space.

Output Format:
Print the elements of the matrix with each row in a new line and elements of each row are separated by a space.

NOTE: There should not be any space after the last element of each row and no new line after the last row.

Example:

Input:
3 3

Output:
1 2 3
4 5 6
7 8 9

Explanation: 
Starting from the first row, the numbers are present in the increasing order. Since it's a 3X3 matrix, the numbers are from 1 to 9. 
'''

r,c = input().split(" ")
r = int(r)
c = int(c)

mat = [[0 for i in range(c)]for j in range(r)]
val = 1
for i in range(r):
    for j in range(c):
        mat[i][j] = val
        val = val+1
for i in range(r):
    for j in range(c):
        if j!=(c-1):
            print (mat[i][j],end=" ")
        else:
            print (mat[i][j],end="")
    if i!=(r-1):
            print() 

