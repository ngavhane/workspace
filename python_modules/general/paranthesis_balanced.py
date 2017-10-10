"""
Implement a function that returns whether a string made of different bracket characters is well formed or not.

For example,
"{({})[]}" is a well formed bracket string
"{[](}" is not a well formed bracket string

Needless to say any single brackets are automatically counted as not well formed
"""




def check_balancing(paren_str):
    parne_dict = {}
    for paren in paren_str:
        if paren
