"""
Description: Check if two strings are anagrams(an improved version using sorted function).
*Anagram: if the strings are different but consists of  same letters
 and form meanigful dictionary words then, it is an anagram.
 *Note: Meanigful words are not checked in here, only the order is checked. 
 @author: Saptarshi Das
"""

#input strings
string1 = input("Enter 1st string: ")
string2 = input("Enter 2nd string: ")

#check for anagrams

#sort both the strings in ascending order and check the equality
if(sorted(string1) == sorted(string2)):
    print ("This are anagrams.")
else:
    print ("This are not anagrams")
