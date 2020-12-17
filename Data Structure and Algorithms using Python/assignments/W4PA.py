'''


Write Python functions as specified below. Paste the text for all functions together into the submission window.

    You may define additional auxiliary functions as needed.
    In all cases you may assume that the value passed to the function is of the expected type, so your function does not have to check for malformed inputs.
    For each function, there are some public test cases and some (hidden) private test cases.
    "Compile and run" will evaluate your submission against the public test cases.
    "Submit" will evaluate your submission against the hidden private test cases and report a score on 100. There are 10 private testcases in all, each with equal weightage.
    Ignore warnings about "Presentation errors".

    We represent scores of batsmen across a sequence of matches in a two level dictionary as follows:

    {'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}

    Each match is identified by a string, as is each player. The scores are all integers. The names associated with the matches are not fixed (here they are 'match1', 'match2', 'match3'), nor are the names of the players. A player need not have a score recorded in all matches.

    Define a Python function orangecap(d) that reads a dictionary d of this form and identifies the player with the highest total score. Your function should return a pair (playername,topscore) where playername is a string, the name of the player with the highest score, and topscore is an integer, the total score of playername.

    The input will be such that there are never any ties for highest total score.

    For instance:

    >>> orangecap({'match1':{'player1':57, 'player2':38}, 'match2':{'player3':9, 'player1':42}, 'match3':{'player2':41, 'player4':63, 'player3':91}})
    ('player3', 100)

    >>> orangecap({'test1':{'Ashwin':84, 'Kohli':120}, 'test2':{'Ashwin':59, 'Pujara':42}})
    ('Ashwin', 143)

    Let us consider polynomials in a single variable x with integer coefficients. For instance:

    3x4 - 17x2 - 3x + 5

    Each term of the polynomial can be represented as a pair of integers (coefficient,exponent). The polynomial itself is then a list of such pairs.

    We have the following constraints to guarantee that each polynomial has a unique representation:
        Terms are sorted in descending order of exponent
        No term has a zero cofficient
        No two terms have the same exponent
        Exponents are always nonnegative 

    For example, the polynomial introduced earlier is represented as:

    [(3,4),(-17,2),(-3,1),(5,0)]

    The zero polynomial, 0, is represented as the empty list [], since it has no terms with nonzero coefficients.

    Write Python functions for the following operations:

    addpoly(p1,p2)
    multpoly(p1,p2)

    that add and multiply two polynomials, respectively.

    You may assume that the inputs to these functions follow the representation given above. Correspondingly, the outputs from these functions should also obey the same constraints.

    You can write auxiliary functions to "clean up" polynomials – e.g., remove zero coefficient terms, combine like terms, sort by exponent etc. Build a library of functions that can be combined to achieve the desired format.

    You may also want to convert the list representation to a dictionary representation and manipulate the dictionary representation, and then convert back.

    Some examples:

      
       >>> addpoly([(4,3),(3,0)],[(-4,3),(2,1)])
       [(2, 1),(3, 0)]

       Explanation: (4x^3 + 3) + (-4x^3 + 2x) = 2x + 3

       >>> addpoly([(2,1)],[(-2,1)])
       []

       Explanation: 2x + (-2x) = 0

       >>> multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)])
       [(1, 3),(-1, 0)]

       Explanation: (x - 1) * (x^2 + x + 1) = x^3 - 1


'''

def orangecap(d):
  totalscore = dict()
  for match in d:
    for player in d[match]:
      if player in totalscore:
        totalscore[player] += d[match][player]
      else:
        totalscore[player] = d[match][player]
  best = max(totalscore, key=totalscore.get)
  return best, totalscore[best]

def addpoly(p1, p2):
  i =0
  j =0
  c =[]
  if len(p1) == 0:
    return p2
  if len(p2) == 0:
    return p1
  while i < len(p1) and j < len(p2):
    if int(p1[i][1]) == int(p2[j][1]):
      sum = p1[i][0] + p2[j][0]
      if sum != 0:
        c.append((sum, p1[i][1]))
      i = i+1
      j = j+1
    elif p1[i][1] > p2[j][1]:
      c.append((p1[i]))
      i = i+1
    elif p1[i][1] < p2[j][1]:
      c.append((p2[j]))
      j = j+1
  if p1[i:] != []:
    for k in p1[i:]:
      c.append(k)
  if p2[j:] != []:
    for k in p2[j:]:
      c.append(k)
  return c

def multpoly(p1, p2):
  p =[]
  for i in p1:
    c =[]
    for j in p2:
      s = i[0] * j[0]
      e = i[1] + j[1]
      c.append((s, e))
    p = addpoly(c, p)

  return p
# Hidden code below

import ast

def todict(inp):
    inp = ast.literal_eval(inp)
    return (inp)

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

def tostring(s):
  lquote = s.find('"')
  rquote = s.rfind('"')
  return(s[lquote+1:rquote])

def tolist(s):
  lbrack = s.find('[')
  rbrack = s.rfind(']')
  slist = s[lbrack+1:rbrack].split(',')
  if slist == ['']:
    slist = []
  else:
    for i in range(0,len(slist)):
      slist[i] = int(slist[i])
  return(slist)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "orangecap":
   arg = todict(farg)
   print(orangecap(arg),end="")
elif fname == "addpoly":
   (arg1,arg2) = topairoflists(farg)
   print(addpoly(arg1,arg2),end="")
elif fname == "multpoly":
   (arg1,arg2) = topairoflists(farg)
   print(multpoly(arg1,arg2),end="")
else:
   print("Function", fname, "unknown")
