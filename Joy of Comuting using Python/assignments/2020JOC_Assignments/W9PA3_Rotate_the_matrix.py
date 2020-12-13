'''
Given a square matrix with n rows and n columns, you have to write a program to rotate this matrix such that each element is shifted by one place in a clockwise manner.
For example, given the following matrix

1 2 3
4 5 6
7 8 9

The output should be

4 1 2
7 5 3
8 9 6

Input Format:
The first line of the input contains a number n representing the number of rows and columns.
After this, there are n rows with each row containing n elements separated by a space

Output Format:
Print the elements of the modified matrix with each row in a new line and all the elements in each row is separated by a space.

Example 1:

Input:
3
1 2 3
4 5 6
7 8 9

Output:
4 1 2
7 5 3
8 9 6

Example 2:
Input:
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Output:
5 1 2 3
9 10 6 4
13 11 7 8
14 15 16 12

Explanation: 
In the first example, there is an odd number of rows and columns hence excluding the middle element i.e. 5 all the elements were shifted by one position in a clockwise manner.
In the second example, there are even number of rows and columns hence all the elements were shifted by one position in a clockwise manner 
'''

# Function to rotate a matrix 
def rotateMatrix(mat): 
  
    if not len(mat): 
        return
      
    """ 
        top : starting row index 
        bottom : ending row index 
        left : starting column index 
        right : ending column index 
    """
  
    top = 0
    bottom = len(mat)-1
  
    left = 0
    right = len(mat[0])-1
  
    while left < right and top < bottom: 
  
        # Store the first element of next row, 
        # this element will replace first element of 
        # current row 
        prev = mat[top+1][left] 
  
        # Move elements of top row one step right 
        for i in range(left, right+1): 
            curr = mat[top][i] 
            mat[top][i] = prev 
            prev = curr 
  
        top += 1
  
        # Move elements of rightmost column one step downwards 
        for i in range(top, bottom+1): 
            curr = mat[i][right] 
            mat[i][right] = prev 
            prev = curr 
  
        right -= 1
  
        # Move elements of bottom row one step left 
        for i in range(right, left-1, -1): 
            curr = mat[bottom][i] 
            mat[bottom][i] = prev 
            prev = curr 
  
        bottom -= 1
  
        # Move elements of leftmost column one step upwards 
        for i in range(bottom, top-1, -1): 
            curr = mat[i][left] 
            mat[i][left] = prev 
            prev = curr 
  
        left += 1
  
    return mat

l=[]
a=int(input())
for i in range(a):
  l1=[x for x in input().split()]
  l.append(l1)
rl=[rotateMatrix(l)]
for i in range(a-1):
  print(' '.join(l[i]))
print(' '.join(l[a-1]),end='')





