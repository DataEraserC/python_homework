def ispal(str):
    reversed_str = str[::-1]
    if str == reversed_str:
        return True
    else:
        return False


num = input("please input a num:")
print(num, ("is" if ispal(num) else "is not"), "pal")
