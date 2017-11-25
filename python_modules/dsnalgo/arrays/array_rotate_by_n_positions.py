"""
Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements.

Example:

Input:  arr[] = [1, 2, 3, 4, 5, 6, 7]
            d = 2
Output: arr[] = [3, 4, 5, 6, 7, 1, 2]
Array

Rotation of the above array by 2 will make array

ArrayRotation1

"""


"Time complexity to solve this probelm is O(n/2)"


def rotate(input_array, count):
    length = len(input_array)

    for index in range(count):
        temp = input_array[index]
        input_array[index] = input_array[length-index-1]
        input_array[length-index-1] = temp
    return input_array
l = [1, 2, 3, 4 , 5,6,7,8,9,10]
print rotate(l, 5)