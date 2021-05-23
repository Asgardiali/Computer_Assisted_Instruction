import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

realAns = num1 * num2
ok = 0

while ok != 1:

    print("How much is {} times {}?".format(num1, num2))
    ans = int(input("Answer: "))

    if ans == realAns:
        print("Very Good !!!")
        ok = 1
    else:
        print("No Try again !!!")
