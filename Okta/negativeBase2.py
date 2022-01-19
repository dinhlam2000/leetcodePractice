def base_negative_two_to_decimal(value):
    sum = 0
    # import pdb; pdb.set_trace()
    for index, val in enumerate(value):
        if val == 1:
            decimal_value = 2 ** index
            if index % 2 == 1:
                decimal_value = decimal_value * -1

            sum = sum + decimal_value
    return sum

def decimal_to_negative_two(value):
    result = []
    while value != 0:
        rem = (value % -2)
        value = value // -2
        if (rem < 0):
            rem = 1
            value = value + 1
        result.append(rem)
    return result


def solution(A, B):
    # write your code in Python 3.6
    target_value = base_negative_two_to_decimal(A) + base_negative_two_to_decimal(B)
    return decimal_to_negative_two(target_value)

input = [0,1,1,0,0,1,0,1,1,1,0,1,0,1,1]
input2 = []
input2 = [1,0,0,1,1,1]

base_negative_two_to_decimal(input)
import pdb; pdb.set_trace()