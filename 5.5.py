import math
def isPrime(num):
    if type(num) != int:
        return False
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
try:
    print(isPrime(eval(input("please input a int here:"))))
except:
    print("please input int!")
