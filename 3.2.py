sum_value = 1
for i in range(1, 365):
    if i % 7 in [4, 5, 6, 0]:
        sum_value *= 1.01
print(sum_value)
