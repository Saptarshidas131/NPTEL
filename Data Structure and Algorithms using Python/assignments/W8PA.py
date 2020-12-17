'''
For this assignment, you have to write a complete Python program.

    You may define additional auxiliary functions as needed.
    In all cases you may assume that the input to your program has the expected format, so your program does not have to check for malformed inputs.
    There are 4 public test cases and 10 (hidden) private test cases.
    "Compile and run" will evaluate your submission against the public test cases.
    "Submit" will evaluate your submission against the hidden private test cases and report a score on 100.
    Ignore warnings about "Presentation errors".

IOI Training Camp 20xx

(INOI 2011)

We are well into the 21st century and school children are taught dynamic programming in class 4. The IOI training camp has degenerated into an endless sequence of tests, with negative marking. At the end of the camp, each student is evaluated based on the sum of the best contiguous segment (i.e., no gaps) of marks in the overall sequence of tests.

Students, however, have not changed much over the years and they have asked for some relaxation in the evaluation procedure. As a concession, the camp coordinators have agreed that students are allowed to drop upto a certain number of tests when calculating their best segment.

For instance, suppose that Lavanya is a student at the training camp and there have been ten tests, in which her marks are as follows.
Test 	  1   	   2   	  3   	   4   	  5   	   6   	   7   	   8   	   9   	  10  
Marks 	  6   	  -5   	  3   	  -7   	  6   	  -1   	  10   	  -8   	  -8   	  8  

In this case, without being allowed to drop any tests, the best segment is tests 5–7, which yields a total of 15 marks. If Lavanya is allowed to drop upto 2 tests in a segment, the best segment is tests 1–7, which yields a total of 24 marks after dropping tests 2 and 4. If she is allowed to drop upto 6 tests in a segment, the best total is obtained by taking the entire list and dropping the 5 negative entries to get a total of 33.

You will be given a sequence of N test marks and a number K. You have to compute the sum of the best segment in the sequence when upto K marks may be dropped from the segment.
Solution hint

For 1 ≤ i ≤ N, 1 ≤ j ≤ K, let Best[i][j] denote the maximum segment ending at position i with at most j marks dropped. Best[i][0] is the classical maximum subsegment or maximum subarray problem. For j ≥ 1; inductively compute Best[i][j] from Best[i][j-1].
Input format

The first line of input contains two integers N and K, where N is the number of tests for which marks will be provided and K is the limit of how many entries may be dropped from a segment.

This is followed by N lines of input each containing a single integer. The marks for test i, i ∈ {1,2,…,N} are provided in line i+1.
Output format

The output is a single number, the maximum marks that can be obtained from a segment in which upto K values are dropped.
Constraints

You may assume that 1 ≤ N ≤ 104 and 0 ≤ K ≤ 102. The marks for each test lie in the range [-104 … 104]. In 40% of the cases you may assume N ≤ 250.

'''
l = []
l.append(0)

for i in range(n):
    x = int(input())
    l.append(x)

best = [[0 for z in range(k+1)] for zz in range(n+1)]

for i in range(1, n+1):
    best[i][0] = max(best[i-1][0]+l[i], l[i])

    for j in range(1, min(i+1, k+1)):
        best[i][j] = max(best[i-1][j]+l[i], best[i-1][j-1])

ans = 0
for i in range(1, n+1):
    ans = max(ans, best[i][k])

print(ans)

