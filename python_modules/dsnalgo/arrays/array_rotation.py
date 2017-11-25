"Time complexity to solve this probelm is O(n/2)"


def rotate(input_array):
    length = len(input_array)

    for index in range(length/2):
        temp = input_array[index]
        input_array[index] = input_array[length-index-1]
        input_array[length-index-1] = temp
    return input_array
l = [1, 2, 3, 4 , 5]
print rotate(l)