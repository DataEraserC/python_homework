def fact_sum(n):
    a = 1
    sum = 0
    for i in range(1,n+1):
        a *= i
        sum += a
    return sum
print(fact_sum(int(input())))
