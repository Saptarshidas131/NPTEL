'''
 Write a program, which will find all such numbers between m and n (both included) such that each digit of the number is an even number.

Input Format:
The first line contains value m and n separated by a comma.

Output Format:
The numbers obtained should be printed in a comma-separated sequence on a single line.

Constraints:
1000<=m<=9000
1000<=n<=9000
'''

m,n = input().split(',')
m = int(m)
n = int(n)

values = []
for i in range(m, n+1):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))
