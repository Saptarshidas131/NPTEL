'''
A panagram is a sentence containing every 26 letters in the English alphabet. Given a string S, check if it is panagram or not.

Input Format:
The first line contains the sentence S.

Output Format:
Print 'YES' or 'NO' accordingly

Example:

Input:
The quick brown fox jumps over the lazy dog

Output:
YES
'''

def checkPanagram(s):
  list=[]
  for i in range(26):
    list.append(False)
  for c in s.lower():
    if not c==" ":
      list[ord(c)-ord('a')]=True
  for ch in list:
    if ch== False:
      return False
  return True
sentence=input()
if(checkPanagram(sentence)):
  print("YES",end="")
else:
  print("NO",end="")
