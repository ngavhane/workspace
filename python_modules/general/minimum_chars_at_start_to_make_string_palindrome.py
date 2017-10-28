"""
Given a string str we need to tell minimum characters to be added at front of string to make string palindrome
Input  : str = "ABC"
Output : 2
We can make above string palindrome as "CBABC"
by adding 'B' and 'C' at front.

Input  : str = "AACECAAAA";
Output : 2
We can make above string palindrome as AAAACECAAAA
by adding two A's at front of string
"""

class Stack(object):
    def __init__(self):
        pass



def check_if_input_is_palindrome(input_str):
    input_list = []
    for char in input_str:
        input_list.append(char)
    print input_list
    input_str_1 = input_list
    input_str_1.reverse()
    p = "".join(input_str_1)
    return input_str == p



def find_number_of_chars(input_str):
    if check_if_input_is_palindrome(input_str):
        return 0




print find_number_of_chars("ABB")











