"""
Description: Check if two strings are anagrams.
*Anagram: if the strings are different but consists of  same letters
 and form meanigful dictionary words then, it is an anagram.
 *Note: Meanigful words are not checked in here, only the order is checked. 
 @author: Saptarshi Das
"""

#input strings
string1 = input("Enter 1st string: ")
string2 = input("Enter 2nd string: ")

#check for anagrams

#calculate string1 ascii sum 
i = 0
sum1 = 0
while(i<len(string1)):
    sum1 += ord(string1[i])
    i += 1
#print ("String1 ascii sum: ",sum1)

#calculate string2 ascii sum
i = 0
sum2 = 0
while(i<len(string2)):
    sum2 += ord(string2[i])
    i += 1
#print ("String2 ascii sum: ",sum2)

#if the sum of the ascii characters of both the strings are same then it is an anagram.
if(sum1 == sum2):
    print ("This is an anagram.")
else:
    print ("This is not an anagram.")
