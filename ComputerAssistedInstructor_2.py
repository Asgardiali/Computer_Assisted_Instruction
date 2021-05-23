import random


class Test:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def askQuestion(self):
        print("How much is {} times {}?".format(self.num1, self.num2))


class Answer:
    def __init__(self, num3, num4):
        self.num3 = num3
        self.num4 = num4

    def correctAnswer(self):
        if self.num3 == 1:
            print("Very good!")
        elif self.num3 == 2:
            print("Excellent!")
        elif self.num3 == 3:
            print("Nice work!")
        else:
            print("Keep up the good work!")

    def incorrectAnswer(self):
        if self.num4 == 1:
            print("No. Please try again.")
        elif self.num4 == 2:
            print("Wrong. Try once more.")
        elif self.num4 == 3:
            print("Don't give up!")
        else:
            print("No. Keep trying.")


ok = 0
while ok != 1:

    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    num3 = random.randint(0, 3)
    num4 = random.randint(0, 3)

    Q1 = Test(num1, num2)
    Ans1 = Answer(num3, num4)
    realAns = Q1.num1 * Q1.num2

    Q1.askQuestion()
    ans = int(input("Answer: "))
    if ans == realAns:
        Ans1.correctAnswer()
        ok = 1
    else:
        Ans1.incorrectAnswer()
