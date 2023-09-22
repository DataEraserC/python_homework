def calc_value(cycle):
    sum_value = 1
    continue_times = 0
    for i in range(1, 365):
        if continue_times == cycle:
            continue_times = 0
            continue
        continue_times += 1
        if continue_times % 7 in [0, 4, 5, 6]:
            sum_value *= 1.01
    return sum_value


print("每十天休息一次{:.2f}".format(calc_value(10)))
print("每十五天休息一次{:.2f}".format(calc_value(15)))
