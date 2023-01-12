def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_sum = sum([x[1] for x in my_list])
    weighted_sum = sum([x[0] * x[1] for x in my_list])
    return weighted_sum / weight_sum
