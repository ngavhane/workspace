
def reverse_integer(input_int):
    output = 0
    while input_int > 0:
        remainder = input_int % 10
        input_int = input_int / 10
        output = output * 10 + remainder
    return output
print reverse_integer(12345)