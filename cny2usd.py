TempStr = input("please input here:")
while TempStr[-1] not in ['N' , 'n']:
    if TempStr[-3:] in [ "cny", "CNY" ]:
        CNY = eval(TempStr[0:-3])
        USD = CNY / 6
        print("{:.2f}CNY is {:.2f}USD".format(CNY,USD))
    elif TempStr[-3:] in [ "usd", "USD" ]:
        USD = eval(TempStr[0:-3])
        CNY = USD * 6
        print("{:.2f}USD is {:.2f}CNY".format(USD,CNY))
    else:
        print("Your input \"{}\" is not right".format(TempStr))
    TempStr = input("please input here:")
