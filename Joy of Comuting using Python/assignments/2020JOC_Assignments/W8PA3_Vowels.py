'''
Given a string S of lowercase letters, remove consecutive vowels from S. After removing, the order of the list should be maintained.

Input Format:

Sentence S in a single line

Output Format:
Print S after removing consecutive vowels

Example:

Input:
your article is in queue

Output:
yor article is in qu

Explanation:

In the first word, 'o' and 'u' are appearing together, hence the second letter 'u' is removed. In the fifth word, 'u', 'e', 'u' and 'e' are appearing together, hence 'e', 'u', 'e' are removed. 
'''

def is_vow(c):
  return ((c=='a') or (c=='e') or (c=='i') or (c=='o') or (c=='u'))
def removeVowels(str):
  print(str[0], end="")
  for i in range(1,len(str)):
    if((is_vow(str[i-1]) != True) or (is_vow(str[i]) != True)):
      print(str[i], end="")
str=input()
removeVowels(str)
