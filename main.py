

print("Welcome to magic 8 ball! Who is the new player name?")

username = input()

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

