def nine_nine():
    for j in range(1,10):
        for i in range(1,j+1):
            print(f"{i}*{j}={i*j}" ,end=" ")
        print()
nine_nine()
