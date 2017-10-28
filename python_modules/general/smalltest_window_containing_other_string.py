""""
Find the smallest window in a string containing all characters of another string
4.2
Given two strings string1 and string2, find the smallest substring in string1
containing all characters of string2 efficiently.
For Example:

Input :  string = "this is a test string"
         pattern = "tist"
Output :  Minimum window is "t stri"
Explanation: "t stri" contains all the characters
              of pattern.

Input :  string = "geeksforgeeks"
         pattern = "ork"
Output :  Minimum window is "ksfor"






Two apprachoes:


1. brute force

generate all subsrings of first string and check if string is there in it

2. efficient way

1- First check if length of string is less than
   the length of given pattern, if yes
       then "no such window can exist ".
2- Store the occurrence of characters of given
   pattern in a hash_pat[].
3- Start matching the characters of pattern with
   the characters of string i.e. increment count
   if a character matches
4- Check if (count == length of pattern ) this
   means a window is found
5- If such window found, try to minimize it by
   removing extra characters from beginning of
   current window.
6- Update min_length.
7- Print the minimum length window.
"""