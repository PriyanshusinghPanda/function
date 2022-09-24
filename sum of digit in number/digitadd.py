def sum_digit(num_add):
    num_add_result = 0
    while num_add > 0:
        num_add_temp = num_add%10
        num_add = num_add//10
        num_add_result=num_add_result+num_add_temp
    return num_add_result
