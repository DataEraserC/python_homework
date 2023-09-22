for i in range(1, 12, 1):
    for j in range(1, 12, 1):
        if i in [1, 6, 11]:
            if j in [1, 6, 11]:
                print("+", end="  ")
            else:
                print("-", end="  ")
        else:
            if j in [1, 6, 11]:
                print("|", end="  ")
            else:
                print(" ", end="  ")
        if j == 11:
            print()
