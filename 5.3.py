def isNum(num_str):
    try:
        num = eval(num_str)
    except:
        return False
    else:
        if type(num) == int or type(num) == float or type(num) == complex:
            return True
        else:
            return False


print(isNum(input("please input a num here:")))
