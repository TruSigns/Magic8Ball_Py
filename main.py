from random import randint

print("Welcome to magic 8 ball! Who is the new player name?")

username = input("Please enter the players now: ")

print("Welcome to magic ball, " + username)


def isPlayerReady():

    print("is the player is ready? Please type YES or NO ")
    check = input().upper()

    while True:
        if check == "YES":
            print("We will continue")
            break
        elif check == "NO":
            print("Please type YES when you're ready")
            return isPlayerReady()


isPlayerReady()

def giveRandomAnswer():

        ask = input("Please ask your question: ")

        randomAnswer = ["you're probably find out",
                        "Some answers shouldn't be ask",
                        "Ask yourself this... Do you believe in god",
                        "The answer you're trying to seek isn't here",
                        "The answer is Yes... but probably no"]

        answer = randomAnswer[randint(0, 5)]
        print(answer)



giveRandomAnswer()