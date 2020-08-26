from random import randint

answer = randint(1, 10)

number = int(input("(1-10)>"))
while answer != number :
    number = int(input("(1-10)>"))

    if answer == number :
        print("当たりです")
    else :
        print("外れです")
