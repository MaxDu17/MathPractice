import time
import csv
import random

def getRange(start, end):
    number_1 = int(round(random.randrange(start, end)))
    number_2 = int(round(random.randrange(start, end)))
    return number_1, number_2

def main():
    random.seed = time.time()
    query = input("This is your mental math practice. What mode do you want? Teens (t), or two-digits (d), or two-and-one (o)\n")
    mode = input("add (a), subtract (s), or multiply (m)?\n")
    number = input("how many rounds do you want?\n")
    print("get ready")
    time.sleep(3)
    num_correct = 0
    for i in range(int(number)):
        if query == 't':
            n1, n2 = getRange(11, 20)
        elif query == 'd':
            n1, n2 = getRange(11, 100)
        else:
            n1 = int(round(random.randrange(2, 10)))
            n2 = int(round(random.randrange(11, 100)))

        start = time.time()
        if mode == 'a':
            result = n1 + n2
            input_ = input("What is {} + {}\n".format(n1, n2))
        elif mode == 's':
            result = n1-n2
            input_ = input("What is {} - {}\n".format(n1, n2))
        else:
            result = n1 * n2
            input_ = input("What is {} X {}\n".format(n1, n2))
        end = time.time()
        time_taken = round((end-start), 3)
        if int(input_) == result:
            num_correct +=1
            input("correct. Your time was {} seconds. Press Enter ({}/{})".format(time_taken, i+1, int(number)))
        else:
            input("incorrect. The answer was {}. Press Enter to continue ({}/{})".format(result, i+1, int(number)))
    print("your final accuracy was {} out of {}".format(num_correct, int(number)))

main()