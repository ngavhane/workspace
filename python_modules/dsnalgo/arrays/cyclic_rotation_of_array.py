"""
Given an array, cyclically rotate the array clockwise by one.

Examples:

Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}


"""


def cyclic_rotate(input_list, count):
    for _ in range(count):
        temp = input_list[len(input_list)-1]
        print input_list[:-1]
        for index, item in enumerate(input_list[:-1]):
            temp = input_list[index+1]
            pass
            input_list[index+1] = input_list[index]
    return input_list




l = [1, 2, 3, 4, 5, 6]
print cyclic_rotate(l, 1)

