import random
true_ans = random.randint(0, 64)
times = 0
max_times = 3
while times != max_times:
    try:
        ans = (int)(input("please guess a num between 0 and 64:\n"))
    except:
        print("your input is not valid! you should input a int num")
        continue
    if true_ans < ans:
        print("your answer is too big!")
        times += 1
        continue
    elif true_ans > ans:
        print("your answer is too small")
        times += 1
        continue
    else:
        if (times == 0):
            print("bingo! your answer is right")
        elif (times == 1):
            print("well! your answer is right")
        elif (times == 2):
            print("good! your answer is right")
if times == 3:
    print("the times your guess reach {0}, the right answers is {1}".format(
        max_times, true_ans))
