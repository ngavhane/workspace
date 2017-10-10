"""
Given an array A of size 'N' and an integer k, find the maximum for each and every contiguous subarray of size k.

Input :

    First line contains 2 space separated integers 'N' and 'k' .
    Second line contains 'N' space separated integers denoting array elements.
    Output:

        Space separated Maximum of all contiguous sub arrays of size k.
        Constraints :

            1<= N <=10^5
            1<= Ai <=10^9
            1<= k <=N
            SAMPLE INPUT
            9 3
            1 2 3 1 4 5 2 3 6
            SAMPLE OUTPUT
            3 3 4 5 5 5 6


"""
def get_output(array_input, number):
    temp = []
    output = []
    for index, item  in enumerate(array_input):
        temp.append(item)
        if index +1 < number:
            pass
        else:
            output.append(max(temp))
            temp.pop(0)
    return output



if __name__ == "__main__":
    final_output = get_output([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)
    print final_output
