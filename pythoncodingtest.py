number=34

score=5

guessed_number1= int(input("Guess number from 1 to 50 :-"))

if guessed_number1 == number:
    print("You guessed it right!")



else:
    print("wrong guess! 1 heart gone ")

    score=score-1

    guessed_number2= int(input("Guess number from 1 to 50 :-"))

if guessed_number2 == number:
    print("You guessed it right!")

else:
    print("wrong guess! 1 heart more gone ")
    score=score-1

    guessed_number3= int(input("Guess number from 1 to 50 :-"))

if guessed_number3 == number:
    print("You guessed it right!")

else:
    print("wrong guess! 1 heart more gone ")
    score=score-1

    guessed_number4= int(input("Guess number from 1 to 50 :-"))


if guessed_number4 == number:
    print("You guessed it right!")

else:
    print("wrong guess! 1 heart more  gone ")
    score=score-1

    guessed_number5= int(input("Guess number from 1 to 50 :-"))

if guessed_number5 == number:
    print("You guessed it right!")

else:
    print("wrong guess! 1 more  heart gone ")
    score=score-1

while score>0:
    print("You have",score,"hearts left")

