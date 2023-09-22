import re

def gcd(x, y):
    if(y==0):
        return x
    else:
        return gcd(y,x%y)
def lcm(x, y):
    return (int)(x * y /gcd(x, y))

while True:
    try:
        input_str = input("please input two number:")
        try:
            input_num_str = re.split(r"\s+",input_str)
            input_num = [int(x) for x in input_num_str]
        except:
            print("your input is", input_str)
            print("input is not valid")
        else:
            print("your input is", input_str)
            if len(input_num) == 2:
                break
            else:
                print("input is not valid")

    except KeyboardInterrupt:
        print("\rexiting........................")
        exit()

print("gcd is",gcd(input_num[0],input_num[1]))
print("lcm is",lcm(input_num[0],input_num[1]))
