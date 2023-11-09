def fib(times):
    a,b=1,1
    for i in range(times-1):
        a,b=b,a+b
    return a
print(fib(int(input())))
